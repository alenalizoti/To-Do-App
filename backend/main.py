from flask import Flask , jsonify, request
import mysql.connector
from flask_cors import CORS


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "todoapp"
)

def searchById(id):
    cursor = mydb.cursor(prepared=True)
    sql = 'select * from tasks where id = ?'
    parametar= (id,)
    cursor.execute(sql,parametar)
    task = cursor.fetchone()
    return task

app = Flask(__name__)
CORS(app)

@app.route('/tasks',methods = ['GET'])
def allTasks():
    cursor = mydb.cursor(dictionary=True)
    sql = "select * from tasks where completed = 0"
    cursor.execute(sql)
    taskovi = cursor.fetchall()
    response_data = {'message':'true','data':taskovi}
    return jsonify (response_data),200

@app.route('/addTask',methods = ['POST'])
def addTask():
    
    data = request.json
    task = data.get('newTask')
    category = data.get('category')

    cursor = mydb.cursor(prepared=True)
    sql = 'insert into tasks (task,completed,kategorija_id) values (?,0,?)'
    parametar = (task,category)
    cursor.execute(sql,parametar)
    mydb.commit()
    return jsonify({'message':"accepted"}), 200

@app.route('/deleteTask/<id>', methods = ['DELETE'])
def deleteTask(id):

    cursor = mydb.cursor(prepared=True)
    sql = 'delete from tasks where id = ?'
    parametar = (id,)
    cursor.execute(sql,parametar)
    mydb.commit()

    return jsonify({'message':'succsess'}),200

@app.route('/getTask/<id>', methods = ['GET'])
def getTask(id):

    cursor = mydb.cursor(prepared=True, dictionary=True)
    sql = 'select * from tasks where id = ?'
    parametar = (id,)
    cursor.execute(sql,parametar)
    task = cursor.fetchone()

    return jsonify({'message': 'succsess','data' : task}) , 200

@app.route('/updateTask/<id>', methods = ['PUT'])
def updateTask(id):

    data = request.json
    task = data['editedTask']
    print(task)
    print(id)
    cursor = mydb.cursor(prepared=True)
    sql = 'update tasks set task = ? where id = ?'
    parametars = (task,id)
    cursor.execute(sql,parametars)
    mydb.commit()

    return jsonify({'message':'radi'})

@app.route('/api/tasks/<id>', methods = ['PUT'])
def api_tasks(id):

    data = request.json
    completed = data['completed']
    # print(completed)
    cursor = mydb.cursor(prepared=True)
    sql = 'update tasks set completed = ? where id = ?'
    parametars = (completed,id)
    cursor.execute(sql,parametars)
    mydb.commit()

    return jsonify({'message':'succsess',"value":completed})

@app.route('/completedTasks', methods = ['GET'])
def completedTasks():

    cursor = mydb.cursor(dictionary=True)
    sql = 'select * from tasks where completed = 1'
    cursor.execute(sql)
    tasks = cursor.fetchall()

    return jsonify({'message':'succsess','data':tasks})

@app.route('/api/category', methods = ['GET'])
def category():
    cursor = mydb.cursor(dictionary=True)
    sql = 'select * from kategorija'
    cursor.execute(sql)
    category = cursor.fetchall()

    return jsonify({'message':'succes','data': category})

app.run(debug=True)
