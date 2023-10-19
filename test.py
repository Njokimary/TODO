##to install flask
##pip install flask

from flask import Flask
##install sqlalchemy by : pip install SQLALchemy and then import it.
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)###created an instance of the Flask class

app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///app.db"##allows us to creat a database