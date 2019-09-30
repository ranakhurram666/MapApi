from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from constants import *

db = SQLAlchemy()


def create_app():
    """
    This method initializes Flask app and creates tables in database as per given
    model in db_models.py if not created already
    :return:
    """
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
    db.init_app(app)

    with app.app_context():
        from . import routes
        # Create tables for our models
        db.create_all()
        return app
