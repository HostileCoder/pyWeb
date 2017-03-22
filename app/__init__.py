from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_rbac import RBAC

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.session_protection = "strong"
lm.login_view = 'login'
lm.init_app(app)

rbac = RBAC()
#rbac.init_app(app)


from app import views, models