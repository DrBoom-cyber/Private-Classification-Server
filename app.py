#Boiler
from flask import Flask, Response, render_template
from flask import jsonify
from flask import request
from flask import Flask

#Authentication
from flask import session
from flask import abort, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

#Backend
from backend import User

app = Flask(__name__)

app.config.update(
    SECRET_KEY = 'temp_key'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

users = [User(id) for id in range(5)]

@app.route('/')
def index():
    return redirect('login');

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users:
            if user.username == username:
                if user.password == password:
                    login_user(user)
                    return redirect('classify')
        return abort(401)
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/classify')
@login_required
def home():
    return render_template('index.html')
