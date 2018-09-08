from flask import Flask
from app import dbconnect
from flask_cors import CORS
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

from app import views#, models
