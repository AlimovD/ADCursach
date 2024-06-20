from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer(), nullable=True)

    bookings = db.relationship('Booking', backref='user', lazy=True)

def __repr__(self):
    return f"<users {{self.username}}>"

class Oteli(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(255), nullable=True)

    bookings = db.relationship('Booking', backref='hotel', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('oteli.id'), nullable=False)
    date_booked = db.Column(db.DateTime, nullable=False, default=datetime.now)
    


def __repr__(self):
    return f"<users {{self.username}}>"