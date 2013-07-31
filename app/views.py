from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN
from app import app, db, lm, oid

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    return render_template('home.html', title="Home", form=form)

@app.route('/store')
def store():
    user = { 'nickname': 'Miguel' } # fake user

    comments = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
            ]
    form = LoginForm()
    return render_template("store.html",
        title = 'Store',
        user = user,
        comments = comments, form=form)

@app.route('/about')
def about():
    form = LoginForm()
    return render_template('about.html', title="About Us",form=form)

@app.route('/faq')
def faq():
    form = LoginForm()
    return render_template('faq.html', title="FAQ",form=form)

@app.route('/contact')
def contact():
    form = LoginForm()
    return render_template('contact.html', title="Contact Us",form=form)

@app.route('/success')
def success():
    form = LoginForm()
    return render_template('success.html', title="Success!",form=form)

@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('success'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', form=form, title="Sign In", providers = app.config['OPENID_PROVIDERS'])

@app.route('/producta')
def producta():
    form= LoginForm()
    return render_template('producta.html', form=form, title="Product A")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


