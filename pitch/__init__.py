from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '08a505fc4b7dbb79a7bd93bccd526901'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://timothy:index506119056@localhost/minutepitch'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Registering blueprints
from pitch.users.routes import users
from pitch.pitches.routes import pitches
from pitch.main.routes import main

app.register_blueprint(users)
app.register_blueprint(pitches)
app.register_blueprint(main)
