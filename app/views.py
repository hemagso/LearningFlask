from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Henrique'} #Fake user
    posts = [
        {'author' : {'nickname' : 'John'}, 'body' : 'Beautiful day in Portland!'},
        {'author' : {'nickname' : 'Susan'}, 'body' : 'The avengers movie was so cool!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID={1}, remember_me={2}'.format(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
