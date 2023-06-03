import os

from app import generate_app


config_object = os.getenv('APP_SETTINGS')
application = generate_app(config_object)
