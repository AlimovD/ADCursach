from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 

from models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'jhiduh38798f8eu3ho3820'
db = SQLAlchemy(app)
app.app_context().push()

with app.app_context():
    db.create_all()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birth = db.Column(db.Date, nullable=False)

    
    def __repr__(self):
        return '<User %r>' % self.id
    

    
@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__': 
    app.run(debug=True)