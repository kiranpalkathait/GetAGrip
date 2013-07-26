from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

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
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form, title="Sign In", providers = app.config['OPENID_PROVIDERS'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')


