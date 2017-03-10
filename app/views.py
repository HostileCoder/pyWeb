from flask import render_template, Response, redirect, url_for, request, session, abort, flash
from flask_login import LoginManager, login_required, login_user,  logout_user, current_user
from app import app,lm
from .logform import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    #user = {'nickname': 'Miguel'}
    user= current_user;
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

			   
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
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
def createAcc():	
    return render_template('createAcc.html')
	
	
@app.route('/')
@app.route('/userProj', methods=['GET', 'POST'])
def userPage():	
    return render_template('userProj.html')	
	
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))  

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))
    