from flask import render_template, flash, redirect, session, url_for, request, g
from forms import LoginForm, ContactForm, ProductForm
from models import User, ROLE_USER, ROLE_ADMIN, Product
import stripe
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid, stripe_keys

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again. ')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me',None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = g.user
    form = LoginForm()
    return render_template('home.html', title="Home", form=form, user=user)

@app.route('/store', methods=['GET','POST'])
def store():
    products = Product.query.all()
    form = LoginForm()
    return render_template("store.html",
        title = 'Store',
      form=form, key=stripe_keys['publishable_key'],products=products)

@app.route('/about')
def about():
    form = LoginForm()
    return render_template('about.html', title="About Us",form=form)

@app.route('/faq')
def faq():
    form = LoginForm()
    return render_template('faq.html', title="FAQ",form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = LoginForm()
    contact = ContactForm()
    return render_template('contact.html', title="Contact Us",form=form, contact=contact)

@app.route('/success')
def success():
    products = Product.query.all()
    form = LoginForm()
    return render_template('success.html', title="Success!",form=form, products=products)

@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', form=form, title="Sign In", providers = app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/producta')
def producta():
    form= LoginForm()
    return render_template('producta.html', form=form, title="Product A")

@app.route('/charge', methods=['POST'])
def charge():
    form = LoginForm()
    return render_template('charge.html', form = form)

@app.route('/admin', methods=['GET','POST'])
def admin():
    form = LoginForm()
    prod = ProductForm()
    if prod.validate_on_submit():
        new = Product(name=prod.name.data, stock=prod.stock.data, image=prod.image.data, price=prod.price.data)
        db.session.add(new)
        db.session.commit()
        flash('Product Added!')
        return redirect(url_for('store'))
    return render_template('admin.html', prod=prod, form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
