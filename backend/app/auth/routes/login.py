import requests

from flask import jsonify
from flask import request
from flask import current_app
from flask_jwt_extended import create_access_token

from app.auth.models import User
from . import auth_bp


@auth_bp.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    if 'code' not in body or body['code'] == '':
        return jsonify(
            detail='Code not provided'
        ), 400

    body = {
        'client_id': current_app.config['TWITCH_CLIENT_ID'],
        'client_secret': current_app.config['TWITCH_CLIENT_SECRET'],
        'code': body['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://localhost:5000/api/auth/login'
    }
    response = requests.post(
        current_app.config['TWITCH_GET_TOKEN_URL'],
        data=body
    ).json()
    if 'access_token' not in response or response['access_token'] == '':
        return jsonify(
            detail='Code not valid!'
        ), 403

    # Get the user from the database
    # If the user does not exist, create it
    user = get_or_register_user(response['access_token'])
    if user is None:
        return jsonify(
            detail='Something went wrong'
        ), 500

    # Generate the JWT access token to APP
    return jsonify(
        access_token=create_access_token(
            identity=user,
            additional_claims={
                'user': {
                    'username': user.login_name,
                    'profile_image_url': user.profile_image_url
                }
            }
        )
    ), 200


def get_or_register_user(access_token):
    twitch_user = get_twitch_user(access_token)
    if twitch_user is None:
        return None

    user = User.get_by_twitch_id(twitch_user['id'])
    if user is None:
        user = User()
        user.public_id = User.generate_public_id()
        user.twitch_id = twitch_user['id']
    user.login_name = twitch_user['login']
    user.email = twitch_user['email']
    user.profile_image_url = twitch_user['profile_image_url']
    user.save()
    return user


def get_twitch_user(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Client-Id': current_app.config['TWITCH_CLIENT_ID']
    }
    response = requests.get(
        current_app.config['TWITCH_GET_USER_URL'],
        headers=headers
    )
    response = response.json()
    if 'data' not in response or len(response['data']) == 0:
        return None

    return response['data'][0]
