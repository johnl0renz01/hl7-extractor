from flask import Blueprint, render_template, request, flash, jsonify, redirect
# from flask_login import login_required, current_user
from .models import Unparsed, MSH_Model, PID_Model, PV1_Model, ORC_Model, OBR_Model, OBX_Model

from . import db
import json
import plotly.express as px
import pandas as pd


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
        
    
def date_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO 8601 string
    raise TypeError(f"Type {type(obj)} not serializable")


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

        # Get data
        pid = getPID(data)
        dob = [item[0] for item in pid]
        dob = json.dumps(dob, default=date_serializer)
        dob = json.loads(dob)

        gender = [item[1] for item in pid]


        # Process data to analyze
        obj = analyzeGender(gender)
        df = pd.DataFrame(obj)
        fig_gender = px.pie(df, names="gender", values="total", title="Gender Distribution")


        obj = analyzeAge(dob)
        df = pd.DataFrame(obj)
        fig_age = px.histogram(df, x="Values", title="Age Distribution", nbins=15)


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


        def figureToHTML(figure):
            return figure.to_html(full_html=False)

        return render_template("index.html", messages=data, sortBy=order, day=day, month=month, year=year, 
                               fig_gender=figureToHTML(fig_gender), fig_age=figureToHTML(fig_age))

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
    
    json_data = data
    json_data = orjson.dumps(json_data).decode("utf-8")
   

    return render_template("result.html", data=data, current_id=id, segment_keys=segments, category=category, json_data=json_data)





###################################################################################################
###################################################################################################
###################################################################################################




import json
import pandas as pd
import plotly.express as px
import plotly.utils  # Import plotly.utils for JSON conversion

@views.route('/piechart', methods=['GET'])
def piechart():
    # Create Pie Chart Data as DataFrame
    df = pd.DataFrame({
        "labels": ["Apple", "Banana", "Cherry"],
        "values": [30, 40, 30]
    })

    # Create Plotly Pie Chart
    fig = px.pie(df, names="labels", values="values", title="Fruit Distribution")

    # Convert Plotly Figure to JSON using plotly.utils
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("piechart.html", graph_json=graph_json)

import json
import plotly.express as px
import pandas as pd
import plotly.io as pio

@views.route('/histogram', methods=['GET'])
def histogram():
    # Create sample data for the histogram
    df = pd.DataFrame({
        "Values": [10, 20, 20, 30, 40, 40, 40, 50, 60, 60, 70, 80, 90, 100, 100,
                   110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
    })

    # Create histogram
    fig = px.histogram(df, x="Values", title="Value Distribution with More Data", nbins=15)

    # fig = px.bar(x=["a", "b", "c", "d", "e", "f"], y=[1,2,3,4,5,6])
    # fig.show()

    fig_html = fig.to_html(full_html=False)


    df = pd.DataFrame({
        "labels": ["Apple", "Banana", "Cherry"],
        "values": [30, 40, 30]
    })

    # Create Plotly Pie Chart
    fig = px.pie(df, names="labels", values="values", title="Fruit Distribution")
    fig_html2 = fig.to_html(full_html=False)

    # Return the HTML with iframe embedding the Plotly figure
    return render_template('histogram.html', fig_html=fig_html, fig_html2=fig_html2)
    
    # Update axis labels
    fig.update_layout(
        xaxis_title="Value",
        yaxis_title="Frequency"
    )

    # Convert Plotly figure to JSON using plotly.io.to_json
    graph_json = json.dumps(pio.to_json(fig))

    return render_template("histogram.html", graph_json=graph_json)

from plotly import utils
from json import dumps

@views.route('/test', methods=['GET'])
def test():
    data = {
        'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'AI': [50, 75, 120, 180, 220, 250, 280],
        'Cloud': [40, 70, 110, 140, 170, 200, 240],
        'Blockchain': [5, 15, 40, 100, 150, 200, 250]
    }

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Create a line plot with Plotly
    fig = px.line(df, x='Year', y=['AI', 'Cloud', 'Blockchain'], title='Publications Over Time')
    fig.update_layout(title='Publications in AI, Cloud, and Blockchain')
    fig.show()
    # turn the figure into a JSON then pass it to the template
    all_pub_json = dumps(fig, cls=utils.PlotlyJSONEncoder)
    return render_template('abc.html', pub_lines_JSON=all_pub_json)



###########################
###########################
# FUNCTIONS


def getPID(data):
    if data:
        filtered_data = []
        for record in data:
            filtered_data.append(record.id)

        return PID_Model.query.with_entities(PID_Model.date_time_of_birth, PID_Model.administrative_sex).filter(PID_Model.unparsed_msg_id.in_(filtered_data)).all()
    else:
        return PID_Model.query.with_entities(PID_Model.date_time_of_birth, PID_Model.administrative_sex).all()


def analyzeAge(data):
    obj = {"Values": []}
    for record in data:
        dob = datetime.fromisoformat(record)

        # Get the current time (timezone-aware), in the same timezone as the dob
        today = datetime.now(dob.tzinfo)  # Use dob's timezone info to get the current time in the same timezone

        # Calculate the age
        age = today.year - dob.year

        obj['Values'].append(age)

    return obj


def analyzeGender(data):
    obj = {"gender": [],
            "total": []}
    for record in data:
        if record.upper() == "M":
            obj['gender'].append("Male")
        elif record.upper() == "F":
            obj['gender'].append("Female")
        else:
            obj['gender'].append("None")

        obj['total'].append(1)

    return obj



# df = pd.DataFrame(obj)

# Custom colors for each category in the 'gender' column
# color_map = {
#     'Male': 'blue',
#     'Female': 'purple',
#     'None': 'green'
# }

# fig = px.pie(df, names="gender", values="total", title="Gender Distribution", color='gender', color_discrete_map=color_map)   # custom color