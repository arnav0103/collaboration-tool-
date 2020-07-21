import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

################

app = Flask(name)

basedir = os.path.abspath(os.path.dirname(file))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
Migrate(app,db)

########### * login config * #################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'loginuser'