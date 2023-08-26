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
    cors.init_app(app, origins='*')

    register_blueprints(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.public_id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        from app.auth.models import User
        identity = jwt_data['sub']
        return User.get_by_public_id(identity)

    return app


def register_blueprints(app: Flask):
    app_bp = Blueprint('app', __name__, url_prefix='/api')

    from app.auth.routes import auth_bp
    app_bp.register_blueprint(auth_bp, url_prefix='/auth')

    from app.pokeapi.routes import pokeapi_bp
    app_bp.register_blueprint(pokeapi_bp, url_prefix='/pokeapi')

    app.register_blueprint(app_bp)
