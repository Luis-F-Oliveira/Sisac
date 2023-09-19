import customtkinter

class Warning(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('300x200')

    def MessageCodi(self, info, codigo):
        avisofont = customtkinter.CTkFont(family='Gill Sans', size=(15))
        aviso = customtkinter.CTkLabel(self, text=f'{info}', font=avisofont)
        aviso.pack(pady=15)

        codigofont = customtkinter.CTkFont(family='Gill Sans', size=(10))
        codigo = customtkinter.CTkLabel(self, text=f'Código: {codigo}', font=codigofont)
        codigo.pack(pady=5)


class WarningException(customtkinter.CTkToplevel):
    def __init__(self, e, defensor, ato, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Aviso: erro')

        error = customtkinter.CTkFrame(self, fg_color=('transparent'))
        error.pack(padx=5)
        label = customtkinter.CTkLabel(
            error,
            text='ERROR:',
            text_color=('red')
        )
        label.pack(side=customtkinter.LEFT)
        label = customtkinter.CTkLabel(
            error,
            text=f'{e}',
            text_color=('yellow')
        )
        label.pack(side=customtkinter.LEFT, padx=(5, 0))

        stop = customtkinter.CTkFrame(self)
        stop.pack(fill=customtkinter.BOTH, pady=5, padx=5)
        label = customtkinter.CTkLabel(
            stop,
            text='Defensor: '
        )
        label.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            stop,
            text=f'{defensor}',
            text_color=('blue')
        )
        label.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            stop,
            text='-> Stop in:'
        )
        label.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            stop,
            text=f'{ato}',
            text_color=('red')
        )
        label.pack(side=customtkinter.LEFT, padx=(5, 0))