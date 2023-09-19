from hashlib import sha256
from tkinter import filedialog
import pandas as pd
import customtkinter
import json
import os

from app.view.warning.warning import Warning
from app.model.system.atualizar import *
from app.model.system.usuarios import *

class Cadastrar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        container1 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container1.pack(pady=(25, 0))
        container2 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container2.pack()
        container3 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container3.pack(pady=(15, 0))

        self.username = customtkinter.CTkEntry(container1, placeholder_text='Username...')
        self.username.pack(side=customtkinter.LEFT, padx=10, pady=10)
        self.password = customtkinter.CTkEntry(container1, placeholder_text='Password...', show='*')
        self.password.pack(side=customtkinter.LEFT, padx=10, pady=10)
        self.user = customtkinter.CTkEntry(container1, placeholder_text='Coplan user...')
        self.user.pack(side=customtkinter.LEFT, padx=10, pady=10)
        self.passw = customtkinter.CTkEntry(container2, placeholder_text='Coplan password...', show='*')
        self.passw.pack(side=customtkinter.LEFT, padx=10, pady=10)
        self.nome = customtkinter.CTkEntry(container2, placeholder_text='Nome...')
        self.nome.pack(side=customtkinter.LEFT, padx=10, pady=10)
        self.cargo = customtkinter.CTkEntry(container2, placeholder_text='Cargo...')
        self.cargo.pack(side=customtkinter.LEFT, padx=10, pady=10)

        btn = customtkinter.CTkButton(container3, text='Sing Up', fg_color=('#43434A'), hover_color=('#2E2E33'), command=self.Commit)
        btn.pack()

        container4 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container4.pack(fill=customtkinter.BOTH, pady=(25, 0), padx=10)

        self.acc = Select()
        self.account = [x[1] for x in self.acc]

        optionmenu = customtkinter.CTkOptionMenu(
            container4,
            values=self.account,
            command=self.optionmenu_callback,
            fg_color=('#43434A'),
            button_color=('#2E2E33')
        )
        optionmenu.pack(side=customtkinter.LEFT)

        self.username_var = customtkinter.StringVar(value="username_off")
        switch = customtkinter.CTkSwitch(
            container4,
            text="Username",
            command=self.switch_event,
            variable=self.username_var,
            onvalue="username_on",
            offvalue="username_off")
        switch.pack(side=customtkinter.RIGHT)

        self.password_var = customtkinter.StringVar(value="password_off")
        switch = customtkinter.CTkSwitch(
            container4,
            text="Password",
            command=self.switch_event,
            variable=self.password_var,
            onvalue="password_on",
            offvalue="password_off")
        switch.pack(side=customtkinter.RIGHT)

        self.user_var = customtkinter.StringVar(value="user_off")
        switch = customtkinter.CTkSwitch(
            container4,
            text="Coplan User",
            command=self.switch_event,
            variable=self.user_var,
            onvalue="user_on",
            offvalue="user_off")
        switch.pack(side=customtkinter.RIGHT)

        self.passw_var = customtkinter.StringVar(value="passw_off")
        switch = customtkinter.CTkSwitch(
            container4,
            text="C Password",
            command=self.switch_event,
            variable=self.passw_var,
            onvalue="passw_on",
            offvalue="passw_off")
        switch.pack(side=customtkinter.RIGHT)

        self.nome_var = customtkinter.StringVar(value="nome_off")
        switch = customtkinter.CTkSwitch(
            container4,
            text="Nome",
            command=self.switch_event,
            variable=self.nome_var,
            onvalue="nome_on",
            offvalue="nome_off")
        switch.pack(side=customtkinter.RIGHT)

        self.cargo_var = customtkinter.StringVar(value="cargo_off")
        switch = customtkinter.CTkSwitch(
            container4,
            text="Cargo",
            command=self.switch_event,
            variable=self.cargo_var,
            onvalue="cargo_on",
            offvalue="cargo_off")
        switch.pack(side=customtkinter.RIGHT)

        self.nivel_var = customtkinter.StringVar(value="nivel_off")
        switch = customtkinter.CTkSwitch(
            container4,
            text="Nivel",
            command=self.switch_event,
            variable=self.nivel_var,
            onvalue="nivel_on",
            offvalue="nivel_off")
        switch.pack(side=customtkinter.RIGHT)

        self.container5 = customtkinter.CTkFrame(self, fg_color=('transparent'), height=28)
        self.container5.pack(fill=customtkinter.BOTH, pady=(25, 0), padx=10)

        container6 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container6.pack(pady=(25, 0), padx=10)

        btnupd = customtkinter.CTkFrame(container6, fg_color=('transparent'))
        btnupd.pack(side=customtkinter.LEFT)
        btn = customtkinter.CTkButton(
            btnupd,
            text='Update',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=self.Update
        )
        btn.pack(padx=10)

        btndlt = customtkinter.CTkFrame(container6, fg_color=('transparent'))
        btndlt.pack(side=customtkinter.LEFT)
        btn = customtkinter.CTkButton(
            btndlt,
            text='Delete',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=self.Delete
        )
        btn.pack(padx=10)
    
    def switch_event(self):
        self.status = []
        self.status.append(self.username_var.get())
        self.status.append(self.password_var.get())
        self.status.append(self.user_var.get())
        self.status.append(self.passw_var.get())
        self.status.append(self.nome_var.get())
        self.status.append(self.cargo_var.get())
        self.status.append(self.nivel_var.get())

        if 'username_on' in self.status:
            if hasattr(self, 'username_entry'):
                self.username_entry.destroy()
            self.username_entry = customtkinter.CTkEntry(self.container5, placeholder_text='Username...')
            self.username_entry.pack(side=customtkinter.LEFT, padx=(0, 10))
        else:
            if hasattr(self, 'username_entry'):
                self.username_entry.destroy()

        if 'password_on' in self.status:
            if hasattr(self, 'password_entry'):
                self.password_entry.destroy()
            self.password_entry = customtkinter.CTkEntry(self.container5, placeholder_text='Password...', show='*')
            self.password_entry.pack(side=customtkinter.LEFT, padx=(0, 10))
        else:
            if hasattr(self, 'password_entry'):
                self.password_entry.destroy()

        if 'user_on' in self.status:
            if hasattr(self, 'user_entry'):
                self.user_entry.destroy()
            self.user_entry = customtkinter.CTkEntry(self.container5, placeholder_text='Coplan User...')
            self.user_entry.pack(side=customtkinter.LEFT, padx=(0, 10))
        else:
            if hasattr(self, 'user_entry'):
                self.user_entry.destroy()

        if 'passw_on' in self.status:
            if hasattr(self, 'passw_entry'):
                self.passw_entry.destroy()
            self.passw_entry = customtkinter.CTkEntry(self.container5, placeholder_text='Coplan Password...', show='*')
            self.passw_entry.pack(side=customtkinter.LEFT, padx=(0, 10))
        else:
            if hasattr(self, 'passw_entry'):
                self.passw_entry.destroy()

        if 'nome_on' in self.status:
            if hasattr(self, 'nome_entry'):
                self.nome_entry.destroy()
            self.nome_entry = customtkinter.CTkEntry(self.container5, placeholder_text='Nome...')
            self.nome_entry.pack(side=customtkinter.LEFT, padx=(0, 10))
        else:
            if hasattr(self, 'nome_entry'):
                self.nome_entry.destroy()

        if 'cargo_on' in self.status:
            if hasattr(self, 'cargo_entry'):
                self.cargo_entry.destroy()
            self.cargo_entry = customtkinter.CTkEntry(self.container5, placeholder_text='Cargo...')
            self.cargo_entry.pack(side=customtkinter.LEFT, padx=(0, 10))
        else:
            if hasattr(self, 'cargo_entry'):
                self.cargo_entry.destroy()

        if 'nivel_on' in self.status:
            if hasattr(self, 'optionmenu'):
                self.optionmenu.destroy()
            self.nive = SelectNivel()
            account = [x[1] for x in self.nive]

            self.optionmenu = customtkinter.CTkOptionMenu(
                self.container5,
                values=account,
                command=self.NivelCallback,
                fg_color=('#43434A'),
                button_color=('#2E2E33')
            )
            self.optionmenu.pack(side=customtkinter.LEFT)
        else:
            if hasattr(self, 'optionmenu'):
                self.optionmenu.destroy()

    def NivelCallback(self, choice):
        selected_nivel = choice
        for nivel_id, tag in self.nive:
            if tag == selected_nivel:
                self.nivel_id = nivel_id
                break

    def optionmenu_callback(self, choice):
        selected_username = choice
        for user_id, username in self.acc:
            if username == selected_username:
                self.selected_user_id = user_id
                break

    def Update(self):
        insert = []
        values = []
        for status in self.status:
            if status == 'username_on':
                insert.append('username')
                values.append(self.username_entry.get())
            if status == 'password_on':
                insert.append('password')
                password = self.password_entry.get()
                sha = sha256(password.encode()).hexdigest()
                values.append(sha)
            if status == 'user_on':
                insert.append('user')
                values.append(self.user_entry.get())
            if status == 'passw_on':
                insert.append('pass')
                values.append(self.passw_entry.get())
            if status == 'nome_on':
                insert.append('nome')
                values.append(self.nome_entry.get())
            if status == 'cargo_on':
                insert.append('cargo')
                values.append(self.cargo_entry.get())
            if status == 'nivel_on':
                insert.append('nivel')
                values.append(self.nivel_id)

        status = UpdateUsers(self.selected_user_id, insert, values)
        match status:
            case 1:
                Warning().MessageCodi('Conta atualizada!', '200')
            case 0:
                Warning().MessageCodi('Conta não foi atualizada!', '400')

    def Commit(self):
        commit = SingUp(
            self.username.get(),
            self.password.get(),
            self.user.get(),
            self.passw.get(),
            self.nome.get(),
            self.cargo.get()
        )

        match commit:
            case 1:
                Warning().MessageCodi(f'Usuário: {self.username.get()},\ncadastrado com SUCESSO!!!', '200')
            case 0:
                Warning().MessageCodi(f'Usuário: {self.username.get()},\nnão foi cadastrado!', '400')

    def Delete(self):
        status = DeletUser(self.selected_user_id)
        match status:
            case 1:
                Warning().MessageCodi('Conta pagada!', '200')
            case 0:
                Warning().MessageCodi('Conta não foi apagada!', '400')

class Banco(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Atualizar Servidores

        container1 = customtkinter.CTkFrame(
            self,
            fg_color=('transparent')
        )
        container1.pack(fill=customtkinter.BOTH)

        labelfont = customtkinter.CTkFont(
            size=20
        )
        label = customtkinter.CTkLabel(
            container1,
            text='Atualizar Banco de Servidores',
            font=labelfont
        )
        label.pack(pady=(20, 10))

        container1system = customtkinter.CTkFrame(
            container1,
            fg_color=('transparent')
        )
        container1system.pack(fill=customtkinter.BOTH)

        commit = customtkinter.CTkButton(
            container1system,
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            text='Atualizar',
            command=self.AtualizarServidor
        )
        commit.pack(side=customtkinter.LEFT, padx=(10, 10))

        file = customtkinter.CTkButton(
            container1system,
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            text='Carregar Arquivo',
            command=self.AbrirArquivo
        )
        file.pack(side=customtkinter.LEFT, padx=(0, 10))

        self.label = customtkinter.CTkLabel(
            container1system,
            text='Sem anexo...'
        )
        self.label.pack(side=customtkinter.LEFT)

        # Manipular Email

        container2 = customtkinter.CTkFrame(
            self,
            fg_color=('transparent')
        )
        container2.pack(fill=customtkinter.BOTH, pady=20)

        label = customtkinter.CTkLabel(
            container2,
            text='Gerencia de E-mails',
            font=labelfont
        )
        label.pack()

        container2system = customtkinter.CTkFrame(
            container2,
            fg_color=('transparent')
        )
        container2system.pack(fill=customtkinter.BOTH)

        adicionar = customtkinter.CTkFrame(
            container2system,
            fg_color=('transparent')
        )
        adicionar.pack(side=customtkinter.LEFT, fill=customtkinter.BOTH, expand=True, padx=10)

        self.email = customtkinter.CTkEntry(
            adicionar,
            placeholder_text='Email'
        )
        self.email.pack(pady=5)
        
        self.password = customtkinter.CTkEntry(
            adicionar,
            placeholder_text='Senha'
        )
        self.password.pack(pady=(5, 10))

        btn = customtkinter.CTkButton(
            adicionar,
            text='Cadastrar',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=self.CadastrarEmail
        )
        btn.pack()

        atualizar = customtkinter.CTkFrame(
            container2system,
            fg_color=('transparent')
        )
        atualizar.pack(side=customtkinter.LEFT, fill=customtkinter.BOTH, expand=True, padx=10)

        self.em = LerEmail()
        self.emails = [x[1] for x in self.em]

        optionmenu = customtkinter.CTkOptionMenu(
            atualizar,
            values=self.emails,
            command=self.optionmenu_callback,
            fg_color=('#43434A'),
            button_color=('#2E2E33')
        )
        optionmenu.pack(pady=5)

        self.email_frame = customtkinter.CTkFrame(
            atualizar,
            fg_color=('transparent')
        )
        self.email_frame.pack(pady=5)

        self.email_var = customtkinter.StringVar(value="email_off")
        switch = customtkinter.CTkSwitch(
            self.email_frame,
            text="Email",
            command=self.switch_event,
            variable=self.email_var,
            onvalue="email_on",
            offvalue="email_off")
        switch.pack(side=customtkinter.LEFT)

        self.senha_frame = customtkinter.CTkFrame(
            atualizar,
            fg_color=('transparent')
        )
        self.senha_frame.pack(pady=5)

        self.senha_var = customtkinter.StringVar(value="senha_off")
        switch = customtkinter.CTkSwitch(
            self.senha_frame,
            text="Senha",
            command=self.switch_event,
            variable=self.senha_var,
            onvalue="senha_on",
            offvalue="senha_off")
        switch.pack(side=customtkinter.LEFT)

        btn_frame = customtkinter.CTkFrame(
            atualizar,
            fg_color=('transparent')
        )
        btn_frame.pack(pady=5)

        btn = customtkinter.CTkButton(
            btn_frame,
            text='Atualizar',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=self.AtualizarEmail
        )
        btn.pack(side=customtkinter.LEFT, padx=5)

        btn = customtkinter.CTkButton(
            btn_frame,
            text='Excluir',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=self.DeleteEmail
        )
        btn.pack(side=customtkinter.LEFT, padx=5)

    def optionmenu_callback(self, choice):
        selected_email = choice
        for email_id, email in self.em:
            if email == selected_email:
                self.selected_email_id = email_id
                break

    def DeleteEmail(self):
        top = customtkinter.CTkToplevel()

        def Sim():
            top.destroy()
            status = DeleteEmail(self.selected_email_id)
            match status:
                case 1:
                    Warning().MessageCodi('Email apagado!', '200')
                case 0:
                    Warning().MessageCodi('Email não apagado.', '400')

        def Nao():
            top.destroy()

        btn_frame = customtkinter.CTkFrame(
            top,
            fg_color=('transparent')
        )
        btn_frame.pack(fill=customtkinter.BOTH, pady=5)

        btn = customtkinter.CTkButton(
            btn_frame,
            text='Excluir',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=Sim
        )
        btn.pack(side=customtkinter.LEFT, padx=5)

        btn = customtkinter.CTkButton(
            btn_frame,
            text='Não excluir',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=Nao
        )
        btn.pack(side=customtkinter.LEFT, padx=5)

    def switch_event(self):
        self.status = []
        self.status.append(self.email_var.get())
        self.status.append(self.senha_var.get())

        if 'email_on' in self.status:
            if hasattr(self, 'email_entry'):
                self.email_entry.destroy()
            self.email_entry = customtkinter.CTkEntry(self.email_frame, placeholder_text='Email...')
            self.email_entry.pack(side=customtkinter.LEFT, padx=10)
        else:
            if hasattr(self, 'email_entry'):
                self.email_entry.destroy()

        if 'senha_on' in self.status:
            if hasattr(self, 'senha_entry'):
                self.senha_entry.destroy()
            self.senha_entry = customtkinter.CTkEntry(self.senha_frame, placeholder_text='Senha...')
            self.senha_entry.pack(side=customtkinter.LEFT, padx=10)
        else:
            if hasattr(self, 'senha_entry'):
                self.senha_entry.destroy()

    def AtualizarEmail(self):
        insert = []
        values = []
        for status in self.status:
            if status == 'email_on':
                insert.append('email')
                values.append(self.email_entry.get())
            if status == 'senha_on':
                insert.append('password')
                values.append(self.senha_entry.get())

        status = UpdateEmail(self.selected_email_id, insert, values)
        match status:
            case 1:
                Warning().MessageCodi('Email atualizado!', '200')
            case 0:
                Warning().MessageCodi('Email não atualizado.', '400')

    def CadastrarEmail(self):
        email = self.email.get()
        senha = self.password.get()
        status = CadastrarEmail(email, senha)
        match status:
            case 1:
                Warning().MessageCodi('Email cadastrado!', '200')
            case 0:
                Warning().MessageCodi('Email não cadastrado.', '400')
    
    def AbrirArquivo(self):
        self.file = filedialog.askopenfilename(
            initialdir="c:/gui/",
            title="Selecionar Arquivo",
            filetypes=(
                ("Arquivos EXCEL", "*.csv"),
                ("Todos os Arquivos", "*.*")
            )
        )
        
        if self.file:
            self.label.configure(text=os.path.basename(self.file))

    def AtualizarServidor(self):
        df = pd.read_csv(self.file, delimiter=";")
        df = df.fillna('sem info')
        df = df[['Matrícula', 'Contrato', 'Servidor', 'EMAIL', 'CARGO']]

        data = df.to_dict(orient='records')

        with open('app/views/json/servidor.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        with open('app/views/json/servidor.json', encoding='UTF-8') as file:
            servidorJson = json.load(file)
        
        Servidores().CleanTable()
        for item in servidorJson:
            Servidores().InsertTable(item['Matrícula'], item['Contrato'], item['Servidor'], item['EMAIL'], item['CARGO'])

class Index(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.add("Usuarios")
        self.add("Atualizar Banco")

        cadastrar = Cadastrar(self.tab("Usuarios"))
        cadastrar.pack(fill=customtkinter.BOTH, expand=True)

        banco = Banco(self.tab("Atualizar Banco"))
        banco.pack(fill=customtkinter.BOTH, expand=True)

class SystemAdmin(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('900x600')
        self.title('Administração')

        index = Index(self)
        index.pack(fill=customtkinter.BOTH, expand=True)