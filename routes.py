from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

<<<<<<< HEAD
@app.route('/log',methods=['GET,POST'])
def log():
    error = none
    if request.method() == 'POST':
        if request.form['username'] != 'admin' or request.form['pasword'] != 'admin':
            error = "WRONG"
        else:
            return redirect(url_for('hello'))
    return render_template('/log')
=======
>>>>>>> ac5f63acb8051fe5405f55473a2f5b3f3744b681
if __name__ == '__main__':
    app.run(host='0.0.0.0')


