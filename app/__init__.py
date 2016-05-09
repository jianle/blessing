from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys
import logging

app = Flask(__name__)
app.config.from_object('config')

reload(sys)
sys.setdefaultencoding('utf-8')

db=SQLAlchemy(app)

logger = logging.getLogger()
logger.setLevel(app.config['LOGGING_LEVEL'])

# create console handler and set level to debug
hander = logging.StreamHandler()
hander.setLevel(app.config.get('LOGGING_LEVEL'))

formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
hander.setFormatter(formatter)
logger.addHandler(hander)
