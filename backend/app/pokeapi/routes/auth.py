import os
import requests
from datetime import datetime
from datetime import timedelta

from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user

from app.auth.models import TokenType
from app.auth.models import Token

from . import pokeapi_bp


CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')
API_URL = os.getenv('TWITCH_GET_USER_URL')


@pokeapi_bp.route('/get_auth_url', methods=['GET'])
@jwt_required()
def get_auth_url():
    token_type = TokenType.query.filter_by(name='POKEAPI').first()
    if token_type is None:
        return jsonify(
            detail='No token type found'
        ), 500

    if CLIENT_ID is None:
        return jsonify(
            detail='No twitch client id found'
        ), 500

    authorize_url = (
        "https://id.twitch.tv/oauth2/authorize"
        "?response_type=code"
        "&client_id={client_id}"
        "&redirect_uri=http://localhost:5173/pokeapi"
        "&scope={token_type}"
    ).format(client_id=CLIENT_ID, token_type=token_type.scopes)

    return jsonify(
        url=authorize_url
    ), 200


@pokeapi_bp.route('/save_token', methods=['POST'])
@jwt_required()
def save_token():
    code = request.get_json()['code']

    get_token_url = "https://id.twitch.tv/oauth2/token"
    body = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost:5173/pokeapi"
    }
    token_data = requests.post(get_token_url, body)
    if token_data is None:
        return jsonify(
            detail='Invalid code!'
        ), 500
    token_data = token_data.json()
    if 'access_token' not in token_data:
        return jsonify(
            detail='Error saving token'
        ), 400

    token_type_id = TokenType.query.filter_by(name='POKEAPI').first().id

    token = Token.query.filter(
        Token.user_id == current_user.id,
        Token.token_type_id == token_type_id
    ).first()

    if token is None:
        token = Token()

    token.access_token = token_data['access_token']
    token.refresh_token = token_data['refresh_token']
    token.expire_date = datetime.utcnow() + timedelta(token_data['expires_in'])
    token.user_id = current_user.id
    token.token_type_id = token_type_id
    token.save()

    return jsonify(
        is_authorized=True
    ), 200


@pokeapi_bp.route('/is_authorized', methods=['GET'])
@jwt_required()
def is_authorized():
    is_authorized = current_user.is_authorized('POKEAPI')

    return jsonify(
        is_authorized=is_authorized
    ), 200
