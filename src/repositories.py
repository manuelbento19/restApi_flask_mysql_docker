from ErrorHandler import AppError
from Mapper import UserMapper

class UsersRepository:
    
    users = []
    
    def __init__(self,connection,context):
        self.connection = connection
        self.context = context
        
    def getAll(self):
        self.context.execute("select * from users")
        for user in self.context.fetchall():
            self.users.append(UserMapper(user))
        return self.users
    
    def findUserById(self,id):
        self.context.execute("select * from users where id=%s",(id,))
        user = self.context.fetchone()
        if user: 
            return UserMapper(user)
    
    def findUserByEmail(self,email):
        self.context.execute("select * from users where email=%s",(email,))
        user = self.context.fetchone()
        if user:
            return UserMapper(user)
    
    def createUser(self,data):
        if "name" not in data: raise AppError("You must insert your name")
        if "email" not in data: raise AppError("You must insert your email")
        if "password" not in data: raise AppError("You must insert your password")

        userExist = self.findUserByEmail(data["email"])
        if userExist: raise AppError("User already exists")

        self.context.execute("insert into users(id,name,email,password) values(DEFAULT,%s,%s,%s)",(data["name"],data["email"],data["password"]))
        self.connection.commit()