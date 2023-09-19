import customtkinter
from tkinter import filedialog
from app.model.email.EmailSearch import EmSql
from app.model.email.EmailEstagiario import EmailEstagiarios
import os

class Estagiario(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=("transparent"))
        self.user = data
        self.email = EmSql()
        self.values = [x[0] for x in self.email]

        infos = customtkinter.CTkFrame(self, fg_color=('transparent'))
        infos.pack(fill=customtkinter.BOTH)

        optionmenu = customtkinter.CTkOptionMenu(
            infos,
            values=self.values,
            command=self.optionmenu_callback,
            fg_color=('#43434A'),
            button_color=('#2E2E33')
        )
        optionmenu.pack(side=customtkinter.LEFT, pady=5)

        self.email_list = []
        self.email = customtkinter.CTkEntry(
            infos,
            placeholder_text='Email do estagiário...'
        )
        self.email.pack(side=customtkinter.LEFT, padx=(5, 0))
        self.email.bind("<Return>", self.addemail)

        self.list_emails = customtkinter.CTkScrollableFrame(
            infos,
            height=30,
            orientation='horizontal',
            fg_color=('transparent')
        )
        self.list_emails.pack(fill=customtkinter.BOTH, pady=(5, 0), padx=(5, 0))

        container1 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container1.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container1,
            text='Exmo. (a) Defensor (a) Público (a),'
        )
        label.pack(side=customtkinter.LEFT)

        container2 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container2.pack(fill=customtkinter.BOTH, pady=(20, 0))
        label = customtkinter.CTkLabel(
            container2,
            text='Comunico, por meio deste, que o (a) estagiário (a)'
        )
        label.pack(side=customtkinter.LEFT)
        self.nome = customtkinter.CTkEntry(
            container2, 
            placeholder_text='Nome Estagiário...'
        )
        self.nome.pack(side=customtkinter.LEFT, padx=5)
        label = customtkinter.CTkLabel(
            container2,
            text='encontra-se'
        )
        label.pack(side=customtkinter.LEFT)


        container3 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container3.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container3,
            text='CONTRATADO (A), conforme solicitado no Processo Nº'
        )
        label.pack(side=customtkinter.LEFT)
        self.resolucao = customtkinter.CTkEntry(
            container3, 
            placeholder_text='Resolução...'
        )
        self.resolucao.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container3,
            text='. Desta'
        )
        label.pack(side=customtkinter.LEFT)
        
        container4 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container4.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container4,
            text='feita, informo que o (a) supracitado (a) estagiário (a) está autorizado (a) a iniciar'
        )
        label.pack(side=customtkinter.LEFT)
        
        container5 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container5.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container5,
            text='suas atividades no dia'
        )
        label.pack(side=customtkinter.LEFT)
        self.data = customtkinter.CTkEntry(
            container5, 
            placeholder_text='Data de inicio...'
        )
        self.data.pack(side=customtkinter.LEFT, padx=5)
        label = customtkinter.CTkLabel(
            container5,
            text='sob vossa supervisão.'
        )
        label.pack(side=customtkinter.LEFT)
        
        container6 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container6.pack(fill=customtkinter.BOTH, pady=20)
        label = customtkinter.CTkLabel(
            container6,
            text='Anexo termo de compromisso assinado.'
        )
        label.pack(side=customtkinter.LEFT)
        
        container7 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container7.pack(fill=customtkinter.BOTH, pady=(0, 20))
        label = customtkinter.CTkLabel(
            container7,
            text='Respeitosamente,'
        )
        label.pack(side=customtkinter.LEFT)
        
        container8 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container8.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container8,
            text=f'{data.nome}'
        )
        label.pack(side=customtkinter.LEFT)
        
        container9 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container9.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container9,
            text=f'{data.cargo}'
        )
        label.pack(side=customtkinter.LEFT)
        
        container10 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container10.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container10,
            text='Coordenadoria de Gestão Funcional'
        )
        label.pack(side=customtkinter.LEFT)
        
        container11 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container11.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container11,
            text='Defensoria Pública do Estado de Mato Grosso'
        )
        label.pack(side=customtkinter.LEFT)
        
        container12 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container12.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container12,
            text='(65) 99954-5349'
        )
        label.pack(side=customtkinter.LEFT)
        
        container13 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container13.pack(fill=customtkinter.BOTH, pady=(20, 5))
        btn = customtkinter.CTkButton(
            container13,
            text='Anexar', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'), 
            command=self.Anexo01
        )
        btn.pack(side=customtkinter.LEFT, padx=(0, 5))
        self.anexo1 = customtkinter.CTkLabel(
            container13, 
            text='Sem anexo...'
        )
        self.anexo1.pack(side=customtkinter.LEFT, padx=(0, 10))

        container14 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container14.pack(fill=customtkinter.BOTH, pady=(5, 20))
        btn = customtkinter.CTkButton(
            container14, 
            text='Anexar', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'), 
            command=self.Anexo02
        )
        btn.pack(side=customtkinter.LEFT, padx=(0, 5))
        self.anexo2 = customtkinter.CTkLabel(
            container14, 
            text='Sem anexo...'
        )
        self.anexo2.pack(side=customtkinter.LEFT, padx=0)

        container15 = customtkinter.CTkFrame(self, fg_color=('transparent'), height=30)
        container15.pack(pady=(0, 10))
        btn = customtkinter.CTkButton(
            container15,
            text='Enviar E-mail',
            width=300,
            height=30,
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'), 
            command=self.Commit
        )
        btn.pack(side=customtkinter.LEFT)

    def Anexo01(self):
        anexo = filedialog.askopenfilename(
            initialdir="c:/gui/",
            title="Selecionar Arquivo",
            filetypes=(
                ("Arquivos PDF", "*.pdf"),
                ("Todos os Arquivos", "*.*")
            )
        )
        
        if anexo:
            self.anexo1.configure(text=os.path.basename(anexo))
            self.anexo01 = anexo

    def Anexo02(self):
        anexo = filedialog.askopenfilename(
            initialdir="c:/gui/",
            title="Selecionar Arquivo",
            filetypes=(
                ("Arquivos PDF", "*.pdf"),
                ("Todos os Arquivos", "*.*")
            )
        )
        
        if anexo:
            self.anexo2.configure(text=os.path.basename(anexo))
            self.anexo02 = anexo

    def optionmenu_callback(self, choice):
        self.selected_email = choice

    def addemail(self, event):
        entered = self.email.get()
        if entered:
            self.email_list.append(entered)
            self.email.delete(0, "end")
            self.update_list_emails()

    def update_list_emails(self):
        for widget in self.list_emails.winfo_children():
            widget.destroy()

        for email in self.email_list:
            label = customtkinter.CTkLabel(
                self.list_emails,
                text=f'{email}'
            )
            label.pack(padx=2, side=customtkinter.LEFT)
        
    def Commit(self):
        if hasattr(self, 'selected_email'):
            selected_email = self.selected_email
            email = self.email_list
            nome = self.nome.get()
            data = self.data.get()
            resolucao = self.resolucao.get()

            arquivo = []
            if hasattr(self, 'anexo01') and self.anexo01:
                arquivo.append(self.anexo01)
            if hasattr(self, 'anexo02') and self.anexo02:
                arquivo.append(self.anexo02)

            EmailEstagiarios(selected_email, email, nome, data, self.user.nome, self.user.cargo, resolucao, arquivo)