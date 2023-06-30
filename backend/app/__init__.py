from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS


db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()


def generate_app(settings='config.development'):
    app = Flask(__name__)
    app.config.from_object(settings)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app_bp = Blueprint('app', __name__, url_prefix='/api')

    from app.auth.routes import auth_bp
    app_bp.register_blueprint(auth_bp, url_prefix='/auth')

    app.register_blueprint(app_bp)
