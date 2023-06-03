""" TEST CASES:
    1. Save user
    2. Get user by private_id
    3. Get user by public_id
    6. Get json formatted user
"""
import pytest
import json

from app.auth.models import User


class TestUserModel():
    """ Test User model """
    @pytest.mark.parametrize('public_id,twitch_id,login_name,expected', [
        ('public_id1', 'twitch_id1', 'login_name1', True),
        ('public_id2', 'twitch_id2', 'login_name2', True),
        ('1107911855855', 'twitch_id3', 'login_name3', False),
        ('public_id4', '52743825', 'login_name4', False),
        ('public_id5', 'twitch_id5', 'Linda', False),
    ])
    def test_create_user(
        self,
        app,
        public_id,
        twitch_id,
        login_name,
        expected
    ):
        """ Test create user
        - Save user only if public_id, twich_id and login_name
          are unique
        - save() method should return True if user is created else False
        """
        with app.app_context():
            user = User()
            user.public_id = public_id
            user.twitch_id = twitch_id
            user.login_name = login_name
            assert user.save() == expected
            assert (user.private_id is not None) == expected

    @pytest.mark.parametrize('private_id,public_id,expected', [
        ('1', 'otro_id1', True),
        ('2', 'otro_id2', True),
        ('3', '8271246117186', False),
        ('4', '7656119744675', False)
    ])
    def test_modify_user(self, app, private_id, public_id, expected):
        """ Test modify user """
        with app.app_context():
            user = User.get_by_private_id(private_id)
            user.public_id = public_id
            assert user.save() == expected

    def test_get_all(self, app):
        """ Test get_all method """
        with app.app_context():
            with open('tests/datatests/models.json') as f:
                data = json.load(f)

            users = User.get_all()
            assert len(users) == len(data['users'])

            for index, user in enumerate(users):
                assert user.public_id == data['users'][index]['public_id']
                assert user.twitch_id == data['users'][index]['twitch_id']
                assert user.login_name == data['users'][index]['login_name']

    @pytest.mark.parametrize('private_id, expected', [
        ('1', '<User 1107911855855>'),
        ('2', '<User 9731607133747>'),
        ('3', '<User 7656119744675>'),
        ('4', '<User 8271246117186>'),
        ('5', '<User 4146572387173>'),
        ('non_existent_id', 'None')
    ])
    def test_get_by_private_id(self, app, private_id, expected):
        """ Test get_by_private_id method """
        with app.app_context():
            user = User.get_by_private_id(private_id)
            assert repr(user) == expected

    @pytest.mark.parametrize('public_id, expected', [
        ('1107911855855', '<User 1107911855855>'),
        ('9731607133747', '<User 9731607133747>'),
        ('7656119744675', '<User 7656119744675>'),
        ('8271246117186', '<User 8271246117186>'),
        ('4146572387173', '<User 4146572387173>'),
        ('non_existent_id', 'None')
    ])
    def test_get_by_public_id(self, app, public_id, expected):
        """ Test get_by_public_id method """
        with app.app_context():
            user = User.get_by_public_id(public_id)
            assert repr(user) == expected

    @pytest.mark.parametrize('twitch_id, expected', [
        ('32313666', '<User 1107911855855>'),
        ('52743825', '<User 9731607133747>'),
        ('54815698', '<User 7656119744675>'),
        ('15581426', '<User 8271246117186>'),
        ('99060640', '<User 4146572387173>'),
        ('non_existent_id', 'None')
    ])
    def test_get_by_twitch_id(self, app, twitch_id, expected):
        """ Test get_by_twitch_id method """
        with app.app_context():
            user = User.get_by_twitch_id(twitch_id)
            assert repr(user) == expected

    @pytest.mark.parametrize('login_name, expected', [
        ('Michelle', '<User 1107911855855>'),
        ('Ethan', '<User 9731607133747>'),
        ('Linda', '<User 7656119744675>'),
        ('Lauren', '<User 8271246117186>'),
        ('Matthew', '<User 4146572387173>'),
        ('non_existent_id', 'None')
    ])
    def test_get_by_login_name(self, app, login_name, expected):
        """ Test get_by_login_name method """
        with app.app_context():
            user = User.get_by_login_name(login_name)
            assert repr(user) == expected
