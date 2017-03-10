from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class LoginForm(Form):
    email = TextField('email', [Required()])
    password = TextField('Password', [Required()])
    remember_me = BooleanField('Remember me')