from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'jhiduh38798f8eu3ho3820'
db = SQLAlchemy(app)

app.app_context().push()

with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            user = User(username=username, password=password)

            try:
                db.session.add(user)
                db.session.commit()
                return redirect('/')
            except:
                return "Ошибка"
        else:
            return render_template("login.html")
        # if user and check_password_hash(user.password, password):
        #     login_user(user)
        #     return redirect(url_for('profile'))
        # else:
        #     flash('Неправильное имя или пароль.')
    return render_template('login.html')

       
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User.query.filter_by(username=username).first()

        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            user = User(username=username, password=password)

            try:
                db.session.add(user)
                db.session.commit()
                return redirect('/')
            except:
                return "Ошибка"
        else:
            return render_template("login.html")

        # if user:
        #     flash('Это имя уже занято, попробуйте еще раз.')
        # else:
        #     hashed_password = generate_password_hash(password)
        #     new_user = User(username=username, password=hashed_password, email=email)
        #     db.session.add(new_user)
        #     db.session.commit()
        #     db.session.close()
        #     login_user(new_user)
        #     flash('Аккаунт успешно создан!')
        # return redirect(url_for('profile'))
    return render_template('register.html')




@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', user=current_user)
    else:
        return redirect(url_for('login'))

    
@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', user=current_user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)