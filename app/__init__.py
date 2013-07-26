from flask import *
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
from app import views
app.config.from_object('config')
db = SQLAlchemy(app)

