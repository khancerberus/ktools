import pytest
import json

from app import generate_app
from app import db
from app.auth.models import User


@pytest.fixture()
def app():
    app = generate_app('config.Testing')

    with app.app_context():
        db.create_all()

        with open('tests/datatests/models.json') as f:
            data = json.load(f)

        for j_user in data['users']:
            user = User()
            user.public_id = j_user['public_id']
            user.twitch_id = j_user['twitch_id']
            user.login_name = j_user['login_name']
            db.session.add(user)
        db.session.commit()

    yield app


# @pytest.fixture()
# def client(app):
#     return app.test_client()
