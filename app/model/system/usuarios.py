from app.database.db import Connect
from hashlib import sha256

db = Connect()

def SingUp(username, password, user, passw, nome, cargo):
    try:
        cursor = db.cursor()

        sha = sha256(password.encode()).hexdigest()

        Insert = f'''
                INSERT INTO `Users`(`username`, `password`, `user`, `pass`, `nome`, `cargo`, `nivel`)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
        '''
        Value = (username, sha, user, passw, nome, cargo, 0)
        cursor.execute(Insert, Value)
        cursor.close()
        db.commit()

        status = 1
    except:
        status = 0
    
    return status

def Select():
    cursor = db.cursor()
    query = 'SELECT user_id, username FROM Users'
    cursor.execute(query)
    acc = cursor.fetchall()
    cursor.close()
    return acc

def SelectNivel():
    cursor = db.cursor()
    query = 'SELECT * FROM Nivel'
    cursor.execute(query)
    nivel = cursor.fetchall()
    cursor.close()
    return nivel

def UpdateUsers(primary_key, insert, values):
    try:
        for x, y in zip(insert, values):
            cursor = db.cursor()    
            upd = f"UPDATE Users SET {x}='{y}' WHERE user_id={primary_key}"
            cursor.execute(upd)
            cursor.close()
            db.commit()

        status = 1
    except:
        status = 0

    return status

def DeletUser(id):
    try:
        cursor = db.cursor()
        dlt = f'DELETE FROM Users WHERE user_id={id}'
        cursor.execute(dlt)
        cursor.close()
        db.commit()

        status = 1
    except:
        status = 0

    return status