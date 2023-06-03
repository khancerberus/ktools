import os

from sqlalchemy.exc import IntegrityError

from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = (
        {'schema': 'auth'}
    ) if os.getenv('APP_SETTINGS') != 'config.Testing' else {}

    private_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(24), nullable=False, unique=True)
    twitch_id = db.Column(db.String(128), nullable=False, unique=True)
    login_name = db.Column(db.String(128), nullable=False, unique=True)
    # tokens = db.relationship('Token', backref='user', lazy=True)

    def save(self):
        try:
            if not self.private_id:
                db.session.add(self)
            db.session.commit()
            return True
        except IntegrityError:
            return False

    def __repr__(self):
        return f'<User {self.public_id}>'

    @staticmethod
    def get_all():
        return db.session.query(User).all()

    @staticmethod
    def get_by_private_id(private_id):
        return db.session.query(User).filter_by(private_id=private_id).first()

    @staticmethod
    def get_by_public_id(public_id):
        return db.session.query(User).filter_by(public_id=public_id).first()

    @staticmethod
    def get_by_twitch_id(twitch_id):
        return db.session.query(User).filter_by(twitch_id=twitch_id).first()

    @staticmethod
    def get_by_login_name(login_name):
        return db.session.query(User).filter_by(
            login_name=login_name
        ).first()
