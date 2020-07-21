from Tool import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64),unique = True,index = True)
    password_hash = db.Column(db.String(128))

    team = db.relationship('Team' , backref = 'user_team', lazy = 'dynamic')
    ownerofteam = db.relationship('Team', backref = 'team_owner', lazy = True)

    def __init__(self, name, email, password):
        self.email = email
        self.name =name
        self.email = email
        self.password_hash = generate_password_hash(password)

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    users = db.relationship(User)
    password_hash = db.Column(db.String(128))

    def __init__(self, name,owner, password):
        self.name = name
        self.users.team_owner = owner
        self.password_hash = generate_password_hash(password)
