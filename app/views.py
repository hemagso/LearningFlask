from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Henrique'} #Fake user
    posts = [
        {'author' : {'nickname' : 'John'}, 'body' : 'Beautiful day in Portland!'},
        {'author' : {'nickname' : 'Susan'}, 'body' : 'The avengers movie was so cool!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)