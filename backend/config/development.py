import os

from .default import * # noqa


DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DB_URI')
