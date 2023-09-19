from app.database.db import Connect
from unidecode import unidecode
import pandas as pd
import json

def Comparativo():
    servidores = []
    with open('app/config/json/epth.json', encoding='utf-8') as fi:
        EmailData = json.load(fi)
    for x in EmailData:
        servidores.append(x['Servidor'])

    db = Connect()
    cursor = db.cursor()
    query = 'SELECT servidor, email FROM Servidores'
    cursor.execute(query)
    ServidorData = cursor.fetchall()
    cursor.close()
    db.close()

    email_servidores = {}
    for servidor_info in ServidorData:
        nome_servidor = unidecode(servidor_info[0]).lower()
        email_servidores[nome_servidor] = servidor_info[1]

    for x in EmailData:
        nome_servidor = unidecode(x['Servidor']).lower()
        if nome_servidor in email_servidores:
            email = email_servidores[nome_servidor]
            x['EMAIL'] = email
        else:
            print(f"Nome: {x['Servidor']}, Email não encontrado")

    # Salvar o EmailData atualizado de volta no arquivo JSON
    with open('app/config/json/epth.json', 'w', encoding='utf-8') as fi:
        json.dump(EmailData, fi, indent=4, ensure_ascii=False)

class XlsxToJson:
    def EmailPonto(xlsx, jsonpath):
        df = pd.read_excel(xlsx)

        df['Data'] = df['Data'].astype(str)
        df['Registro Ímpar'] = df['Registro Ímpar'].astype(str)
        df['Horário'] = df['Horário'].astype(str)
        
        df = df.fillna('nan')
        data = df.to_dict(orient='records')

        with open(jsonpath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        Comparativo()

    def Folha(xlsx, jsonpath):
        df = pd.read_excel(xlsx)
        df = df.fillna('sem info')
        data = df.to_dict(orient='records')

        with open(jsonpath, 'w') as file:
            json.dump(data, file, indent=4)