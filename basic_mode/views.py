from flask import Blueprint, render_template, request, flash, jsonify, redirect
# from flask_login import login_required, current_user
from .models import Unparsed
from . import db
import json

from .parser import parseData

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        msg = request.form.get('content')
        if len(msg) <= 0:
            flash('Message is too short!', category='error') 
        else:
            new_message = Unparsed(content=msg)  #providing the schema 
            db.session.add(new_message) #adding to the database 
            db.session.commit()
            flash('Message added!', category='success')

        return redirect('/')
    else:
        data = Unparsed.query.order_by(Unparsed.date_created).all()
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
    msg = Unparsed.query.get_or_404(id)
    data = parseData(msg.content)

    return render_template("result.html", data=data)