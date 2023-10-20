##to install flask
##pip install flask

from flask import Flask, jsonify, request
##install sqlalchemy by : pip install SQLALchemy and then import it.
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)###created an instance of the Flask class


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"##allows us to creat a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONW'] = False ##used ro reduce the memory usage

db = SQLAlchemy(app) ## create a db variable and add an instance app.SQLAlchemy is used to make queries to the database
app.app_context().push()
#create classes
class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True, index =True)
    name = db.Column(db.String(32),nullable = False)
    description = db.Column(db.String(32), nullable = False)

db.create_all()

##endpoint
@app.route('/')
def welcome():
    return "Welcome"

@app.route('/getToDo')
def getToDo():
    todo_list= []

    todo = TODO.query.all()
    for todo in todo:
        todoObj={
            'id':todo.id,
            'name':todo.name,
            'description':todo.description
        }
        todo_list.append(todoObj)
    return jsonify(todo_list)
    

@app.route('/postToDo',methods = ['POST'])
def addTodo():
    name = request.form['name']
    description = request.form['description']
    ##add it to the table 
    todo = TODO(name=name, description=description)
    db.session.add(todo)
    db.session.commit()
    return "Todo created sucessfully"

if __name__ == '__main__':
    app.run(debug=True)