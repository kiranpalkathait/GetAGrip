from flask import *
from functools import wraps
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('success'))
    return render_template('home.html', error=error, title="Home")

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

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
    return render_template("store.html",
        title = 'Store',
        user = user,
        comments = comments)

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/faq')
def faq():
    return render_template('faq.html', title="FAQ")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")

@app.route('/success')
def success():
    return render_template('success.html', title="Success!")

@app.route('/log', methods=['GET','POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success'))
    return render_template('log.html', error=error, title="Log In")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title="Sign In")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


