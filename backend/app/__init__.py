from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def generate_app(config_object='config.Development'):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)

    return app
