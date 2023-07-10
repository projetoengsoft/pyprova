from dataclasses import dataclass
from .. import db


@dataclass
class User(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    email:str = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name:str = db.Column(db.String(1000))
    profile_type:int = db.Column(db.Integer)