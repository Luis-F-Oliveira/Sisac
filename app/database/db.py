import mysql.connector

def Connect():
    try:
        connection = mysql.connector.connect(
            host='blucaju.com.br',
            user='blucaj55_admin',
            password='eugostodemacarrao',
            database='blucaj55_sisac',
            port='3306',
        )
        if connection.is_connected():
            print("Conexão bem-sucedida ao banco de dados!")
            return connection
    except mysql.connector.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None