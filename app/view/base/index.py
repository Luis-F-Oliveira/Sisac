import customtkinter

class BaseContent(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, **kwargs)
        self.data = data