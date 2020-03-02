from .db import db


class Users(db.Document):
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)
    balance = db.IntField(required=True)