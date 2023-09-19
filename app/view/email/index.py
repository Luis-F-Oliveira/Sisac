import customtkinter
from app.view.base.index import BaseContent
from app.view.email.components.ponto1 import PontoXlsxSystem
from app.view.email.components.ponto2 import PontoWriteSystem
from app.view.email.components.estagiarios import Estagiario

Container = None

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self.configure(fg_color=('transparent'))

class BtnFrame(customtkinter.CTkFrame):
    def __init__(self, master, frame, data, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self.configure(fg_color=('transparent'))

        self.frame = frame
        self.data = data

        btn = customtkinter.CTkButton(master=self, text='Ponto Extenso', fg_color=('#43434A'), hover_color=('#2E2E33'), command=self.Btn2)
        btn.pack(padx=10, side=customtkinter.RIGHT)

        btn = customtkinter.CTkButton(master=self, text='Estagiário', fg_color=('#43434A'), hover_color=('#2E2E33'), command=self.Btn3)
        btn.pack(padx=10, side=customtkinter.RIGHT)

        btn = customtkinter.CTkButton(master=self, text='Email Ponto', fg_color=('#43434A'), hover_color=('#2E2E33'), command=self.Btn1)
        btn.pack(padx=10, side=customtkinter.RIGHT)

    def Btn1(self):
        global Container
        if Container:
            Container.destroy()
        Container = PontoXlsxSystem(self.frame, self.data)
        Container.pack(fill=customtkinter.BOTH)

    def Btn2(self):
        global Container
        if Container:
            Container.destroy()
        Container = PontoWriteSystem(self.frame, self.data)
        Container.pack(fill=customtkinter.BOTH, padx=5)

    def Btn3(self):
        global Container
        if Container:
            Container.destroy()
        Container = Estagiario(self.frame, self.data)
        Container.pack(fill=customtkinter.BOTH, padx=5)

class Content(customtkinter.CTkScrollableFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        frame = Frame(master=self)
        BtnFrm = BtnFrame(master=self, frame=frame, data=data)
        BtnFrm.pack(fill=customtkinter.BOTH, pady=10)
        frame.pack(fill=customtkinter.BOTH, pady=(15, 0))

class EmailContent(BaseContent):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, data, **kwargs)
        self.data = data

        index = Content(master=self, data=self.data)
        index.pack(fill=customtkinter.BOTH, expand=True)