##to install flask
##pip install flask

from flask import Flask
##install sqlalchemy by : pip install SQLALchemy and then import it.
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)###created an instance of the Flask class

app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///app.db"##allows us to creat a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONW'] = False ##used ro reduce the memory usage

db = SQLAlchemy(app) ## create a db variable and add an instance app.SQLAlchemy is used to make queries to the database

#create classes
class TODO(db.Model):
    id = db.Column(db.Interger, primary_key=True, index =True)
    name = db.Column(db.String(32),nullable = False)
    description = db.Column(db.String(32), nullable = False)

db.create_all()