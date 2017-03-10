from flask import Flask, Response
from flask_login import LoginManager, UserMixin, login_required
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True, unique=True)
    project = db.relationship('Project', backref='author', lazy='dynamic')
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)
        
class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)