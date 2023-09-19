from app.database.db import Connect

def EmSql():
    db = Connect()
    cursor = db.cursor()
    query = 'SELECT email FROM Emails'
    cursor.execute(query)
    email = cursor.fetchall()
    cursor.close()
    db.close()

    return email

def EmailPassword(email):
    db = Connect()
    cursor = db.cursor()
    query = f'SELECT password FROM Emails WHERE email="{email}"'
    cursor.execute(query)
    password = cursor.fetchall()
    cursor.close()
    db.close()

    return password