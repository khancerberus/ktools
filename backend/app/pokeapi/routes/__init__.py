from flask import Blueprint


pokeapi_bp = Blueprint('pokeapi', __name__)

from . import auth  # noqa
