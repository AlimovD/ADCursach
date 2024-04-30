from flask_login import UserMixin
from models import User, db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class User(UserMixin, db.Model):

    db = SQLAlchemy()
    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(50), unique=True)
        psw = db.Column(db.String(500), nullable=True)
        date = db.Column(db.DataTime, default=datetime.utcnow)

        def __repr__(self):
            return f"<users {self.id}>"
        
    class Profiles(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=True)
        old = db.Column(db.Integer)
        city = db.Column(db.String(100))
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

        def __repr__(self):
            return f"<users {self.id}>"