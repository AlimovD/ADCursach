from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 


from models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'jhiduh38798f8eu3ho3820'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
    
@app.route('/create-article')
def create_article():
    return render_template()


with app.app_context(): 
    db.create_all() 


if __name__ == '__main__': 
app.run(debug=True)