import os

from dotenv import load_dotenv

from app import generate_app

load_dotenv()
settings = os.getenv('APP_SETTINGS', 'config.development')
application = generate_app(settings)
