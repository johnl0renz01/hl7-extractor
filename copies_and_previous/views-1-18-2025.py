from flask import Blueprint, render_template, request, flash, jsonify, redirect
# from flask_login import login_required, current_user
from .models import Unparsed, MSH_Model, PID_Model, PV1_Model, ORC_Model, OBR_Model, OBX_Model

from . import db
import json

from sqlalchemy import func
from parser import parseData
from hl7apy.parser import parse_message

views = Blueprint('views', __name__)



def validateMessage(data):
    try:
        if "|ORU" in data:
            data = data.replace("|ORU","|OR_")

        hl7_message = f"""{data}"""
        message = parse_message(hl7_message)
        return True
    except Exception:
        return False

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        msg = request.form.get('content')

        if len(msg) <= 0:
            flash('Message is too short!', category='error') 
        elif not validateMessage(msg):
            flash('Invalid message content!', category='error') 
        else:
            new_message = Unparsed(content=msg)  # providing the schema 
            db.session.add(new_message) # adding to the database 
            db.session.commit()

            # get the last id of this message row
            current_id = db.session.query(func.max(Unparsed.id)).scalar()

            # pass the id in parseData
            parseData(msg, current_id)

            flash('Message added!', category='success')

        return redirect('/')
    else:
        page = request.args.get('page', 1, type=int)

        data = Unparsed.query.order_by(Unparsed.date_created.desc()).paginate(page=page, per_page=5)
        return render_template("index.html", messages=data)

@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    msg = Unparsed.query.get_or_404(id)

    if request.method == 'POST':
        msg.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', message=msg)


@views.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    msg_id = Unparsed.query.get_or_404(id)

    try:
        db.session.delete(msg_id)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
    

@views.route('/result/<int:id>', methods=['GET'])
def extract(id):
    data = {}

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
    
        
    # else:
    #     getData("msh", MSH_Model)
    #     getData("pid", PID_Model)
    #     getData("pv1", PV1_Model)
    #     getData("orc", ORC_Model)
    #     getData("obr", OBR_Model)
    #     getData("obx", OBX_Model)

    # return jsonify(data)
    
    return render_template("result.html", data=data, current_id=id, segment_keys=segments, category=category)