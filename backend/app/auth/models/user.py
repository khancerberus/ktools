import secrets

from utils.database import try_save
from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'auth'}

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(24), nullable=False, unique=True)
    twitch_id = db.Column(db.String(128), nullable=False, unique=True)
    login_name = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    profile_image_url = db.Column(db.String(256), nullable=False)

    tokens = db.relationship('Token', backref='user', lazy=True)

    def json(self):
        return {
            'public_id': self.public_id,
            'twitch_id': self.twitch_id,
            'login_name': self.login_name
        }

    def save(self):
        return try_save(self)

    def is_authorized(self, application):
        if application is None:
            return False

        if self.tokens is None:
            return False

        has_token = [
            token for token in self.tokens  # type: ignore
            if token.token_type.name == application
        ]

        return len(has_token) != 0

    def __repr__(self):
        return f'<User {self.public_id}>'

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_private_id(private_id):
        return User.query.filter_by(private_id=private_id).first()

    @staticmethod
    def get_by_public_id(public_id):
        return User.query.filter_by(public_id=public_id).first()

    @staticmethod
    def get_by_twitch_id(twitch_id):
        return User.query.filter_by(twitch_id=twitch_id).first()

    @staticmethod
    def get_by_login_name(login_name):
        return User.query.filter_by(login_name=login_name).first()

    @staticmethod
    def generate_public_id():
        new_public_id = secrets.token_hex(12)
        if User.get_by_public_id(new_public_id):
            return User.generate_public_id()
        return new_public_id
