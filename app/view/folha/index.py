import customtkinter
from app.view.base.index import BaseContent
from app.view.folha.components.acumulo import AcumuloFrame

class FolhaPagamento(BaseContent):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, data, **kwargs)
        self.configure(fg_color=("transparent"))
        self.data = data

        acumulo = AcumuloFrame(self, data=self.data)
        acumulo.pack(fill=customtkinter.BOTH, pady=5, padx=5)