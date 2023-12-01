def UserMapper(user):
    return {
        "id": user[0],
        "name": user[1],
        "email": user[2],
        "password": user[3]
    }