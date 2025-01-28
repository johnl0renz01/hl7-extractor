from flask import Blueprint, render_template, request, flash, jsonify, redirect
# from flask_login import login_required, current_user
from .models import Unparsed, MSH_Model, PID_Model, PV1_Model, ORC_Model, OBR_Model, OBX_Model

from . import db
import json
from collections import OrderedDict
import orjson

from sqlalchemy import func
from .utils.parser import parseData
from .utils.convertor import convertMessage
from datetime import datetime

from hl7apy.parser import parse_message

views = Blueprint('views', __name__)


def validateMessage(data):
    try:
        data = convertMessage(data)[0]

        hl7_message = f"""{data}"""
        return parse_message(hl7_message)
    except Exception:
        return False


def processMessage(request, type, current_id=None):
    msg = request.form.get('content')

    if len(msg) <= 0:
        flash('Message is too short!', category='error') 
    elif not validateMessage(msg):
        flash('Invalid message content!', category='error') 
    else:
        if type == 'create':
            new_message = Unparsed(content=msg)  # providing the schema 
            db.session.add(new_message) # adding to the database 
            db.session.commit()

            # get the last id of this message row
            current_id = db.session.query(func.max(Unparsed.id)).scalar()
        elif type == 'update':
            msg_id = Unparsed.query.get_or_404(current_id)
            db.session.delete(msg_id)
            db.session.commit()
            new_message = Unparsed(id=current_id, content=msg)  # providing the schema 
            db.session.add(new_message) # adding to the database 
            db.session.commit()

        # pass the id in parseData
        parseData(msg, current_id)

        if type == 'create':
            flash('Message added!', category='success')
        elif type == 'update':
            flash('Message updated!', category='success')
        


@views.route('/', methods=['GET', 'POST'])
def home():
    order, day, month, year = '', '', '', ''

    if request.method == 'POST': 
        processMessage(request, 'create')
        return redirect('/')
    else:
        page = request.args.get('page', 1, type=int)
        order = request.args.get("order")

        day = request.args.get("day")
        month = request.args.get("month")
        year = request.args.get("year")

        if day:
            data = Unparsed.query.filter(func.date(Unparsed.date_created)==day)
        elif month:
            data = Unparsed.query.filter(func.to_char(Unparsed.date_created,'YYYY-MM').like(f"{month}%"))
        elif year:
            data = Unparsed.query.filter(func.to_char(Unparsed.date_created,'YYYY').like(f"{year}%"))
        else:
            data = None


        if order == "oldest":
            if data:
                data = data.order_by(Unparsed.date_created.asc()).paginate(page=page, per_page=5)
            else:
                data = Unparsed.query.order_by(Unparsed.date_created.asc()).paginate(page=page, per_page=5)
        else:
            if data:
                data = data.order_by(Unparsed.date_created.desc()).paginate(page=page, per_page=5)
            else:
                data = Unparsed.query.order_by(Unparsed.date_created.desc()).paginate(page=page, per_page=5)
            

        return render_template("index.html", messages=data, sortBy=order, day=day, month=month, year=year)

@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    msg = Unparsed.query.get_or_404(id)

    if request.method == 'POST':
        try:
            processMessage(request, 'update', id)
            return redirect(f'/update/{id}')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', message=msg)


@views.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    msg = Unparsed.query.get_or_404(id)

    try:
        db.session.delete(msg)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
    

# Custom serializer
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO 8601 string
    raise TypeError(f"Type {type(obj)} not serializable")
    

@views.route('/result/<int:id>', methods=['GET'])
def extract(id):
    data = {}

    json_data = {"asd": "z"}

    def getData(segment_str, segment_model):
        segment = segment_model.query.filter_by(unparsed_msg_id=id).all()
            
        if len(segment) <= 0:
            data[segment_str] = {"data": None}
            return None
            

        segment_row = [row.as_dict() for row in segment]

        

        for current_segment in segment_row:
            del current_segment['id'] # remove id column
            del current_segment['unparsed_msg_id'] # remove unparsed_msg_id column  

        
            for key, val in current_segment.items():
                if isinstance(val, str):
                    if '{' in val and '}' in val:
                        val = val.replace('{','')
                        val = val.replace('}', '')
                        val = val.split(',')
                        current_segment[key] = val
                        
        if len(segment_row) == 1:
            segment_row = segment_row[0]

        data[segment_str] = segment_row

        # Return valid segment
        return segment_row

    
    segments = {'msh': MSH_Model, 'pid': PID_Model, 'pv1': PV1_Model, 'orc': ORC_Model, 'obr': OBR_Model, 'obx': OBX_Model}
    empty_segments = []

    for key, val in segments.items():
        result = getData(key, val)
        if not result:
            empty_segments.append(key)

    

    for idx in range(len(empty_segments)):
        del segments[empty_segments[idx]]

    category = request.args.getlist("category")
    if len(category) >= 1:
        data = {}
        for item in category:
            if item in segments:
                value = segments[item]
                getData(item, value)      
    
    json_data = data
    json_data = orjson.dumps(json_data).decode("utf-8")
   

    return render_template("result.html", data=data, current_id=id, segment_keys=segments, category=category, json_data=json_data)
