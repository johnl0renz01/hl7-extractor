from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("DATABASE_URL")
# connection = psycopg2.connect(URL)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = URL
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    
    with app.app_context():
        db.create_all()

    # Define the custom filter function
    def is_list(value):
        return isinstance(value, list)
    
    def append_to_list(existing_list, new_item):
        existing_list.append(new_item)
        return existing_list

    # Register the custom filter with Flask's Jinja2 environment
    app.jinja_env.filters['is_list'] = is_list
    app.jinja_env.globals.update(append_to_list=append_to_list)

    return app
