import os

from .default import * # noqa


TESTING = True
DEBUG = False
SQLALCHEMY_DATABASE_URI = os.getenv('TESTING_DB_URI')
