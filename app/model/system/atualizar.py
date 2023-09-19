from app.database.db import Connect

db = Connect()

class Servidores:
    def __init__(self):
        self.cursor = db.cursor()
        
    def CleanTable(self):
        self.cursor.execute(
            'DELETE FROM Servidores'
        )
        db.commit()

    def InsertTable(self, matricula, contrato, servidor, email, cargo):
        ist = 'INSERT INTO `Servidores` (`matricula`, `contrato`, `servidor`, `email`, `cargo`) VALUES (%s, %s, %s, %s, %s)'
        values = (matricula, contrato, servidor, email, cargo)
        self.cursor.execute(ist, values)
        db.commit()

def CadastrarEmail(email, senha):
    try:
        cursor = db.cursor()
        ist = 'INSERT INTO Emails (email, password) VALUES (%s, %s)'
        values = (email, senha)
        cursor.execute(ist, values)
        db.commit()
        cursor.close()
        
        status = 1
    except:
        status = 0

    return status

def LerEmail():
    cursor = db.cursor()
    query = 'SELECT email_id, email FROM Emails'
    cursor.execute(query)
    email = cursor.fetchall()
    cursor.close()
    return email

def UpdateEmail(primary_key, insert, values):
    try:
        for x, y in zip(insert, values):
            cursor = db.cursor()    
            upd = f"UPDATE Emails SET {x}='{y}' WHERE email_id={primary_key}"
            cursor.execute(upd)
            cursor.close()
            db.commit()

        status = 1
    except:
        status = 0

    return status

def DeleteEmail(id):
    try:
        cursor = db.cursor()
        dlt = f'DELETE FROM Emails WHERE email_id=%s'
        values = (id,)
        cursor.execute(dlt, values)
        db.commit()
        cursor.close()

        status = 1
    except:
        status = 0

    return status