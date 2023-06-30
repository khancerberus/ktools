""" Test login
- login() should return a 400 status code if the code is not provided
- login() should return a 403 status code if the code is not valid
- login() should return a 200 status code if the user is logged in
- login() should return a access_token for webapp if the user is logged in
"""
import pytest

from app.auth.routes.login import get_or_register_user


class TestLogin():
    """ Test the user login for app """
    def test_code_provided(self, client):
        """ login() should return a 400 status code if the code is not provided
        """
        response = client.post('/api/auth/login', json={
            'code': ''
        })
        assert response.status_code == 400
        assert response.json['detail'] == 'Code not provided'

    def test_code_valid(self, client):
        """ login() should return a 403 status code if the code is not valid
        """
        response = client.post('/api/auth/login', json={
            'code': 'not_valid_code'
        })
        assert response.status_code == 403
        assert response.json['detail'] == 'Code not valid!'

    def test_user_logged_in(self, client):
        """ login() should return a 200 status code if the user is logged in
        """
        response = client.post('/api/auth/login', json={
            'code': 'valid_code'
        })
        assert response.status_code == 200
        assert 'access_token' in response.json


class TestGetOrRegisterUser():
    """ Test the get_or_register_user() function """
    @pytest.mark.usefixtures("app_ctx")
    @pytest.mark.parametrize('twitch_id, expected', [
        ('twitch_id_1', '<User 1>'),
        ('twitch_id_2', '<User 2>'),
        ('twitch_id_3', '<User 3>'),
        ('twitch_id_4', '<User 4>')
    ])
    def test_get_or_register_user(self, twitch_id, expected):
        """ get_or_register_user() should return a user if it exists
        """
        getted_user = get_or_register_user(twitch_id)
        assert repr(getted_user) == expected
