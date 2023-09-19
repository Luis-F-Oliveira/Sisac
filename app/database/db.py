import mysql.connector

def Connect():
    try:
        connection = mysql.connector.connect(
            host='',
            user='',
            password='',
            database='',
            port='3306',
        )
        if connection.is_connected():
            print("Conexão bem-sucedida ao banco de dados!")
            return connection
    except mysql.connector.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None
