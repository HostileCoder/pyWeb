from flask import render_template, Response, redirect, url_for, request, session, abort, flash
from flask_login import LoginManager, login_required, login_user,  logout_user, current_user
from app import app,lm,rbac,db,models
from .logform import LoginForm
from .models import User, Project
from dpd import url,headers
import requests
import base64

@app.route('/')
@app.route('/index')
@rbac.allow(['user','admin'], methods=['Get','POST'])
@login_required
def index():      
    user = current_user
    project = Project.query.filter_by(user_id=user.id).first()
    #users = project.users
    return render_template("index.html",
                           title='Home',
                           user=user,
                           project=project)

			   
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
@rbac.allow(['anonymous'], methods=['GET', 'POST'])
def login():
   
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password==form.password.data:
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.html',form=form)

 
@app.route('/')
@app.route('/createAcc', methods=['GET', 'POST'])
@rbac.allow(['user','admin'], methods=['Get','POST'])
def createAcc():	
    return render_template('createAcc.html')
	
	
@app.route('/')
@app.route('/userList', methods=['GET', 'POST'])
@rbac.allow(['admin'], methods=['Get','POST'])
def userList():	
    #session.clear()
    return render_template('userList.html')	
    
@app.route('/')    
@app.route('/invite/<id>')
@rbac.allow(['user','admin'], methods=['Get','POST'])
@login_required
def invite(id):
    project=Project.query.get(id)
    users=User.query.all()
    user=current_user
    Cuser= current_user
    invited_users= project.users
    return render_template('invite.html',project=project, 
                                         users=users, 
                                         Cuser=Cuser, invited_users=invited_users)	

@app.route('/')    
@app.route('/inviteUser',methods=['GET', 'POST'])
def inviteUser():

    user= current_user
    p=Project.query.filter_by(user_id=user.id).first()
     
    for i in request.form.getlist('invited'):  
        u = models.User.query.get(i)
        p.users.append(u)
    
    db.session.add(p)
    db.session.commit()
    
    return redirect(url_for('index'))
    
	
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))  

@app.route('/logout')
@rbac.allow(['user','admin'], methods=['Get','POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))
    
