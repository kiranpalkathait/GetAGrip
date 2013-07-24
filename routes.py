from flask import *
from functools import wraps
app = Flask(__name__)

app.secret_key = "my precious"

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('success'))
    return render_template('home.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/store')
def store():
    return render_template('store.html',title="Store")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    title="FAQ"
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/log', methods=['GET','POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success'))
    return render_template('log.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


