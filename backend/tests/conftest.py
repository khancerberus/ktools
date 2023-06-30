import pytest

from app import generate_app
from app import db

from app.auth.models import User


@pytest.fixture()
def app():
    app = generate_app('config.testing')

    with app.app_context():
        db.create_all()

        users = [
            {
                'public_id': '1',
                'twitch_id': 'twitch_id_1',
                'login_name': 'login_name_1',
                'email': 'email_1'
            }, {
                'public_id': '2',
                'twitch_id': 'twitch_id_2',
                'login_name': 'login_name_2',
                'email': 'email_2'
            }, {
                'public_id': '3',
                'twitch_id': 'twitch_id_3',
                'login_name': 'login_name_3',
                'email': 'email_3'
            }
        ]
        for user in users:
            new_user = User()
            new_user.public_id = user['public_id']
            new_user.twitch_id = user['twitch_id']
            new_user.login_name = user['login_name']
            new_user.email = user['email']
            new_user.save()

        yield app

        # WARN If you change the settings for generating the app, you may need
        # to comment this teardown code.
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def app_ctx(app):
    with app.app_context():
        yield
