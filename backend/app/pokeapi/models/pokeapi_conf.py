from app import db


class PokeAPIConf(db.Model):  # TODO Refactor to PokeAPIAuth
    __tablename__ = 'pokeapi_conf'
    __table_args__ = {'schema': 'pokeapi'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', backref='pokeapi_conf', lazy=True)

    def __repr__(self):
        return '<PokeAPIConf %r>' % self.name

# from app import generate_app
# application = generate_app('config.development')
# with application.app_context():
#   db.creat_all()
