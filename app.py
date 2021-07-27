#Boiler
from flask import Flask, Response, render_template
from flask import jsonify
from flask import request
from flask import Flask

#Authentication
from flask import session
from flask import abort, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

#Database
from flask_sqlalchemy import SQLAlchemy

#Create application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Local database objects
from database import User

app.config.update(
    SECRET_KEY = 'temp_key'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username = username).first()
        if not user is None:
            if user.verify_password(password):
                login_user(user)
                return url_for('classify')
            else:
                return abort(401, description = 'Password is incorrect')
        else:
            return abort(401, description = 'User not found')
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user(current_user)
    return Response('<p>Logged out</p>')

@app.errorhandler(401)
def page_not_found(e):
    return Response(f'<p>Login failed: {e.description}</p>')

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id = user_id).first()

@app.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    return render_template('index.html', name = current_user.username)

@app.route('/classify', methods = ['GET', 'POST'])
@login_required
def classify():
    if request.method == 'GET':
        get_next = request.form.get('get-item')
        if not get_next is None and get_next is True:
            return {
                'image_path': 'static\\assets\image\\filler.jpg',
                'hash' : 'pretend_hash'
            }
        else:
            data = {
                'image_path' : 'static\\assets\image\\filler.jpg',
                'hash' : 'pretend_hash'
            }
            return render_template('index.html', image_data = data, labels = {'a': 'letter_a', 's': 'letter_s', 'd': 'letter_d'})
    elif request.method == 'POST':
        label = request.form['label']
        hash = request.form['hash']
        #resolve item