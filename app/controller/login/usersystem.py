from app.database.db import Connect
from app.model.login.searchuser import *
from hashlib import sha256

class User:
    def __init__(self, id, username, password, user, passw, nome, cargo, nivel):
        self.id = id
        self.username = username
        self.password = password
        self.user = user
        self.passw = passw
        self.nome = nome
        self.cargo = cargo
        self.nivel = nivel

    def __repr__(self):
        return f'<User: {self.username}>'
    
class UserLoginSystem:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = Users()

    def Validacao(self):
        sha = sha256(self.password.encode()).hexdigest()
        for UserData in self.data:
            if UserData.username == self.username and UserData.password == sha:
                return UserData
        
        return None