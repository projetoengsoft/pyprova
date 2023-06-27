from ..config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(128))