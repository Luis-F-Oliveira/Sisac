import customtkinter
from tkinter import filedialog
import os
from app.controller.folha.commit import Fcommit

class AcumuloFrame(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, **kwargs)
        self.data = data

        container1 = customtkinter.CTkFrame(self)
        container1.pack(fill=customtkinter.BOTH, padx=5, pady=5)
        labelfont = customtkinter.CTkFont(size=30)
        label = customtkinter.CTkLabel(
            container1,
            font=labelfont,
            text='Lançamento de acumulo'
        )
        label.pack()

        container2 = customtkinter.CTkFrame(self, fg_color=('transparent'))
        container2.pack(fill=customtkinter.BOTH, padx=5, pady=(0, 5))
        btn = customtkinter.CTkButton(
            container2,
            text='Anexar', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=self.OpenFile
        )
        btn.pack(side=customtkinter.LEFT)
        self.label = customtkinter.CTkLabel(
            container2,
            text='Sem anexo...',
            text_color=('red')
        )
        self.label.pack(side=customtkinter.LEFT, padx=5)
        btn = customtkinter.CTkButton(
            container2,
            text='Iniciar', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=self.Commit
        )
        btn.pack(side=customtkinter.RIGHT)

    def OpenFile(self):
        self.Anexo = filedialog.askopenfilename(
            initialdir="c:/gui/",
            title="Selecionar Arquivo",
            filetypes=(
                ("Arquivos EXCEL", "*.xlsx"),
                ("Todos os Arquivos", "*.*")
            )
        )
        
        if self.Anexo:
            self.label.configure(
                text=os.path.basename(self.Anexo), 
                text_color=('green')
            )

    def Commit(self):
        toplevel = customtkinter.CTkToplevel()
        def Yes():
            toplevel.destroy()
            Fcommit(self.Anexo, self.data.user, self.data.passw).Commit()

        def No():
            toplevel.destroy()

        h1 = customtkinter.CTkLabel(
            toplevel, 
            text='Tudo pronto para começar?'
        )
        h1.pack(pady=(0, 10))

        botoes = customtkinter.CTkFrame(toplevel, fg_color=('transparent'))
        botoes.pack(fill=customtkinter.BOTH, padx=10, pady=(0, 10))
        btn = customtkinter.CTkButton(
            botoes, text='Sim', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'), 
            command=Yes
        )
        btn.pack(side=customtkinter.LEFT, padx=(0, 10))
        btn = customtkinter.CTkButton(
            botoes, 
            text='Não', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'), 
            command=No
        )
        btn.pack(side=customtkinter.RIGHT)