from flask import *
from functools import wraps
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form, title="Sign In", providers = app.config['OPENID_PROVIDERS'])

if __name__ == '__main__':
    app.run(debug=True)


