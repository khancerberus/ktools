from utils.database import try_save
from app import db


class Token(db.Model):
    __tablename__ = 'token'
    __table_args__ = {'schema': 'auth'}

    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String(128), nullable=False, unique=True)
    refresh_token = db.Column(db.String(128), unique=True)
    expire_date = db.Column(db.DateTime, unique=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('auth.user.id')
    )
    token_type_id = db.Column(
        db.Integer,
        db.ForeignKey('auth.token_type.id'),
        nullable=False
    )

    def save(self):
        return try_save(self)

    def __repr__(self):
        return f'<Token {self.id}>'
