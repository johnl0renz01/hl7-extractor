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
    # from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')

    # from .models import User, Note
    
    with app.app_context():
        db.create_all()

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))


    # Define the custom filter function
    def is_list(value):
        return isinstance(value, list)

    # Register the custom filter with Flask's Jinja2 environment
    app.jinja_env.filters['is_list'] = is_list

    return app


# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
