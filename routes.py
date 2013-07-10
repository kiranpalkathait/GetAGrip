from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def derp():
    return render_template('derp.html')

if __name__ == '__main__':
    app.run()


