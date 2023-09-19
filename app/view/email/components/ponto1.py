import customtkinter
from tkinter import filedialog
from app.model.email.EmailSearch import EmSql
from app.controller.xlsxtojson import XlsxToJson
from app.model.email.EmailPonto import EmailPontoEnviar
import json

class PontoXlsxSystem(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self.configure(fg_color=('transparent'))
        self.user = data

        self.xlsxfile = filedialog.askopenfilename(
            initialdir='c:/gui/',
            title='Selecionar Arquivo',
            filetypes=(
                ('Arquivos EXCEL', '*xlsx'),
                ('Todos os Arquivos', '*.*')
            )
        )

        XlsxToJson.EmailPonto(self.xlsxfile, 'app/config/json/epth.json')

        head = customtkinter.CTkFrame(self, fg_color=('transparent'))
        head.pack(fill=customtkinter.BOTH, padx=10, pady=10)

            #  primeiro container
        container1 = customtkinter.CTkFrame(head, fg_color=('transparent'))
        container1.pack(fill=customtkinter.BOTH)

        self.email = EmSql()
        self.values = [x[0] for x in self.email]

        optionmenu = customtkinter.CTkOptionMenu(
            container1,
            values=self.values,
            command=self.optionmenu_callback,
            fg_color=('#43434A'),
            button_color=('#2E2E33')
        )
        optionmenu.pack(side=customtkinter.LEFT, padx=(0, 5))

        username = customtkinter.CTkLabel(container1, text=f'{data.nome}')
        username.pack(side=customtkinter.LEFT)

        btn = customtkinter.CTkButton(
            container1,
            text='Enviar',
            fg_color=('#43434A'),
            hover_color=('#2E2E33'),
            command=self.Commit
        )
        btn.pack(side=customtkinter.RIGHT)

            #  segundo container

        container2 = customtkinter.CTkFrame(head, fg_color=('transparent'))
        container2.pack(fill=customtkinter.BOTH, pady=(5, 0))

        self.titulo = customtkinter.CTkEntry(
            container2,
            placeholder_text='Titulo'
        )
        self.titulo.pack(side=customtkinter.LEFT, padx=(0, 5))
        self.procedimento = customtkinter.CTkEntry(
            container2,
            placeholder_text='Procedimento'
        )
        self.procedimento.pack(side=customtkinter.LEFT)
        
        body = customtkinter.CTkScrollableFrame(self, orientation='horizontal', height=275)
        body.pack(fill=customtkinter.BOTH, padx=10, pady=10)

        with open('app/config/json/epth.json', encoding='UTF-8') as file:
            headings = json.load(file)

        for x in headings:
            col = customtkinter.CTkFrame(master=body)
            col.pack(fill=customtkinter.BOTH, side=customtkinter.LEFT, expand=True)

            h1 = customtkinter.CTkLabel(master=col, text=f'{x["Servidor"]}', width=180, height=30)
            h1.pack(padx=2, pady=2, fill=customtkinter.BOTH)

            p = customtkinter.CTkLabel(master=col, text=f'{x["Data"]}', width=180, height=30)
            p.pack(pady=2, padx=2)

            p = customtkinter.CTkLabel(master=col, text=f'{x["Registro Ímpar"]}', width=180, height=30)
            p.pack(pady=2, padx=2)

            p = customtkinter.CTkLabel(master=col, text=f'{x["Horário"]}', width=180, height=30)
            p.pack(pady=2, padx=2)
            
            p = customtkinter.CTkLabel(master=col, text=f'{x["Carga Horária Insuficiente"]}', width=180, height=30)
            p.pack(pady=2, padx=2)

            p = customtkinter.CTkLabel(master=col, text=f'{x["Mês"]}', width=180, height=30)
            p.pack(pady=2, padx=2)

            p = customtkinter.CTkLabel(master=col, text=f'{x["Ano"]}', width=180, height=30)
            p.pack(pady=2, padx=2)

            p = customtkinter.CTkLabel(master=col, text=f'{x["EMAIL"]}', width=180, height=30)
            p.pack(pady=2, padx=2)

    def optionmenu_callback(self, choice):
        self.selected_email = choice

    def Commit(self):
        if hasattr(self, 'selected_email'):
            selected_email = self.selected_email
            assinatura = self.user.nome
            title = self.titulo.get()
            procedimento = self.procedimento.get()

            EmailPontoEnviar(title, assinatura, self.user.cargo, procedimento, selected_email)