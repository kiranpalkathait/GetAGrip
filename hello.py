from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/helloderp')
def derp_page():
    return 'Derp'

if __name__ == '__main__':
    app.run()
