from flask import Flask,request
import json, database
from ErrorHandler import AppError
from repositories import UsersRepository
from Mapper import UserMapper


app = Flask(__name__)

db = database.createConnection()
connection = db[0]
context = db[1]

usersRepository = UsersRepository(connection,context)

@app.route('/')
def index():
    return {
        "message": "v1 - UsersAPI with Flask"
    }

@app.route('/user',methods=["GET"])
def getUsers():
    users = usersRepository.getAll()
    return users

@app.route('/user/<id>')
def getUserById(id):
    try:
        user = usersRepository.findUserById(id)
        if user == None: raise AppError("User doesn't exists")
        return user
    
    except Exception as error:
        if isinstance(error,AppError):
            return {
                "error": str(error)
            },404
        else:
            return {
                "error": "Bad Request"
            },500
        
@app.route('/user',methods=["POST"])
def createUser():
    try:
        body = json.loads(request.data)
        usersRepository.createUser(body)
        
        return {
            "message": "User created"
        }, 201
        
    except Exception as error:
        if isinstance(error,AppError):
            return {
                "error": str(error)
            },400
        else:
            print(error)
            return {
                "error": "Bad Request"
            },500

@app.errorhandler(404)
def notFound(error):
    print(error)
    return {
        "error": "Page Not Found"
    }

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")