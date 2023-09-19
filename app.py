from app.controller.login.usersystem import UserLoginSystem
from app.view.base.index import BaseContent
from app.view.admin.system import SystemAdmin
from app.view.email.index import EmailContent
from app.view.folha.index import FolhaPagamento

from functools import partial
import customtkinter
import json

class Content(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self.current_content = None

    def show_content(self, content_class, data):
        if self.current_content:
            self.current_content.destroy()

        self.current_content = content_class(self, data=data)
        self.current_content.pack(fill=customtkinter.BOTH, expand=True)

class Exploration(customtkinter.CTkScrollableFrame):
    def __init__(self, master, content_instance, data, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self.content_instance = content_instance

        with open('app/config/json/explorbtn.json', encoding='UTF-8') as file:
            btn_data = json.load(file)

        if data.nivel == 6:
            login = customtkinter.CTkButton(self, text='Sistema', fg_color=('#43434A'), hover_color=('#2E2E33'), command=SystemAdmin)
            login.pack(pady=(5, 15))

        for item in btn_data:
            text = item["TEXT"]
            command = item["Command"]
            button_function = partial(self.execute_command, command, data)
            required_nivel = item["Nivel"]

            if data.nivel in required_nivel or data.nivel == 6:
                btn = customtkinter.CTkButton(self, text=text, fg_color=('#43434A'), hover_color=('#2E2E33'), command=button_function)
                btn.pack(pady=5)

    def execute_command(self, command, data):
        try:
            content_class = globals().get(command)
            if content_class and issubclass(content_class, BaseContent):
                if isinstance(self.content_instance, Content):
                    self.content_instance.show_content(content_class, data)
                else:
                    print("Error: 'content_instance' is not an instance of Content.")
            else:
                eval(command)(master='', data=data)
        except Exception as e:
            print(f"Error executing command: {e}")


class Container(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

class Login(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('SISAC')
        self.geometry('280x400')

        TituloFont = customtkinter.CTkFont(family='Gill Sans', size=40)
        titulo = customtkinter.CTkLabel(master=self, text='Login', font=TituloFont)
        titulo.pack(pady=15)

        self.username = customtkinter.CTkEntry(master=self, placeholder_text='Username...', width=250)
        self.username.pack(pady=(0, 15))

        self.password = customtkinter.CTkEntry(master=self, placeholder_text='Password...', show='*', width=250)
        self.password.pack()

        entrar = customtkinter.CTkButton(master=self, text='ENTRAR', width=250, height=30, fg_color=('#43434A'), hover_color=('#2E2E33'), command=self.system)
        entrar.pack(pady=(45, 0))

    def system(self):
        username = self.username.get()
        password = self.password.get()

        uls = UserLoginSystem(username, password)
        data = uls.Validacao()
        
        if data is not None and data != []:
            self.destroy()
            app = App(data)
            app.mainloop()
        else:
            warning = customtkinter.CTkLabel(master=self, text='Usuário/Senha inválidos!')
            warning.pack(pady=(5, 0))

class App(customtkinter.CTk):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(f'SISAC - {data.username}')
        self.geometry('780x450')

        self.data = data

        container = Container(master=self)
        container.pack(fill=customtkinter.BOTH, expand=True)

        content = Content(master=container)
        content.pack(side=customtkinter.RIGHT, fill=customtkinter.BOTH, expand=True)

        exploration = Exploration(master=container, content_instance=content, data=self.data)
        exploration.pack(side=customtkinter.LEFT, fill=customtkinter.BOTH)

if __name__=="__main__":
    login = Login()
    login.mainloop()