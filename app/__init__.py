from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db=SQLAlchemy(app)

from .main import main
from .main.user import user
