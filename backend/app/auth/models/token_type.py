from utils.database import try_save
from app import db


class TokenType(db.Model):
    __tablename__ = 'token_type'
    __table_args__ = {'schema': 'auth'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    scoops = db.Column(db.String(256), nullable=False, unique=False)

    tokens = db.relationship('Token', backref='token_type', lazy=True)

    def save(self):
        return try_save(self)

    def __repr__(self):
        return f'<TokenType {self.id}>'
