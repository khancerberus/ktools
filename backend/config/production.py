import os

from .default import * # noqa


DEBUG = False
SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_DB_URI')
