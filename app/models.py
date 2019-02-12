from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    Pitches =db.relationship('Pitch',backref = 'user', lazy ='dynamic')

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    Pitches =db.relationship('Pitch', backref = 'category', lazy ='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    upVotes = db.Column(db.Integer, default = 0)
    downVotes = db.Column(db.Integer, default = 0)
    category_id = db.Column(db.Integer, db.ForeignKey( "categories.id" ))
    user_id = db.Column(db.Integer, db.ForeignKey( "users.id" ))

    def __repr__(self):
        return f'User {self.message}'

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category_id = id).all()
        return pitches
