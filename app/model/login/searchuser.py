from app.database.db import Connect

def SearchUser():
    db = Connect()
    cursor = db.cursor()
    query = 'SELECT * FROM Users'
    cursor.execute(query)
    acc = cursor.fetchall()
    return acc

def Users():
    from app.controller.login.usersystem import User
    Query = SearchUser()
    users = []
    for x in Query:
        users.append(User(id=x[0], username=x[1], password=x[2], user=x[3], passw=x[4], nome=x[5], cargo=x[6], nivel=x[7]))
    return users