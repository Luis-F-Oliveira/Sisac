import customtkinter
from app.model.email.EmailSearch import EmSql
from app.model.email.EmailPonto import PontoExtend

Content = None

class ShowWrite(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=("transparent"))

        container1 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container1.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container1,
            text='Informo que a justificativa deve ser encaminhada contendo ciência da chefia imediata,'
        )
        label.pack(side=customtkinter.LEFT)

        container2 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container2.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container2,
            text='e ser pautada em algumas das hipóteses previstas na RESOLUÇÃO Nº 037/2022/DPG.'
        )
        label.pack(side=customtkinter.LEFT)

        container3 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container3.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container3,
            text='Em caso de não apresentação da justificativa, será realizado o desconto proporcional'
        )
        label.pack(side=customtkinter.LEFT)

        container4 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container4.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container4,
            text='nos vencimentos.'
        )
        label.pack(side=customtkinter.LEFT, pady=(0, 15))

        container5 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container5.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container5,
            text='Sendo assim, fica estabelecido prazo de 5 (cinco) dias úteis para apresentação da'
        )
        label.pack(side=customtkinter.LEFT)

        container6 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container6.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container6,
            text='justificativa, que deverá ser encaminhada como resposta a este e-mail.'
        )
        label.pack(side=customtkinter.LEFT, pady=(0, 15))

        container7 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container7.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container7,
            text='Caso tenha aberto o procedimento anterior à notificação para justificar a inadimplência,'
        )
        label.pack(side=customtkinter.LEFT)

        container8 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container8.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container8,
            text='informar seu respectivo número. Entretanto, após a notificação da irregularidade,'
        )
        label.pack(side=customtkinter.LEFT)

        container9 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container9.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container9,
            text='a justificativa deverá ser encaminhada em resposta ao e-mail SEM abertura'
        )
        label.pack(side=customtkinter.LEFT)

        container10 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container10.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container10,
            text='de novo procedimento.'
        )
        label.pack(side=customtkinter.LEFT, pady=(0, 15))

        container11 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container11.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container11,
            text='AS MANIFESTAÇÕES DEVEM SER ACOMPANHADAS DA CIÊNCIA DA CHEFIA IMEDIATA'
        )
        label.pack(side=customtkinter.LEFT)
        
        container12 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container12.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container12,
            text='EM RESPOSTA A ESSE E-MAIL.'
        )
        label.pack(side=customtkinter.LEFT, pady=(0,15))
        
        container13 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container13.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container13,
            text='Ficamos à disposição para eventuais esclarecimentos.'
        )
        label.pack(side=customtkinter.LEFT, pady=(0,15))
        
        container14 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container14.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container14,
            text='Respeitosamente,'
        )
        label.pack(side=customtkinter.LEFT)

        container15 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container15.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container15,
            text=f'{data.nome}'
        )
        label.pack(side=customtkinter.LEFT)

        container16 = customtkinter.CTkFrame(self, fg_color=("transparent"))
        container16.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container16,
            text=f'{data.cargo}'
        )
        label.pack(side=customtkinter.LEFT)

class PontoWriteSystem(customtkinter.CTkFrame):
    def __init__(self, master, data, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=("transparent"))
        self.data = data
        self.email = EmSql()
        self.values = [x[0] for x in self.email]
        
        buttons = customtkinter.CTkFrame(self, fg_color=("transparent"))
        buttons.pack(pady=(0, 10))

        btn = customtkinter.CTkButton(
            buttons, 
            text='Ausência', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=self.Ausencia
        )
        btn.pack(side=customtkinter.LEFT)

        btn = customtkinter.CTkButton(
            buttons, 
            text='Único', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=self.Registro
        )
        btn.pack(side=customtkinter.LEFT, padx=5)

        btn = customtkinter.CTkButton(
            buttons, 
            text='Insuficiência', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=self.Insuficiencia
        )
        btn.pack(side=customtkinter.LEFT)

    def Ausencia(self):
        global Content
        if Content:
            Content.destroy()
        Content = customtkinter.CTkFrame(self, fg_color=("transparent"))
        Content.pack(fill=customtkinter.BOTH)

        container1 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container1.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container1,
            text='De ordem do Excelentíssimo Diretor Geral, conforme o procedimento'
        )
        label.pack(side=customtkinter.LEFT)
        self.procedure = customtkinter.CTkEntry(
            container1,
            placeholder_text='Procedimento'
        )
        self.procedure.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container1,
            text=','
        )
        label.pack(side=customtkinter.LEFT)
        
        container2 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container2.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container2,
            text='vimos muito respeitosamente notificar Vossa Senhoria para apresentação de'
        )
        label.pack(side=customtkinter.LEFT)
        
        container3 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container3.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container3,
            text='justificativa quanto À AUSÊNCIA DE REGISTRO na data de'
        )
        label.pack(side=customtkinter.LEFT)
        self.date = customtkinter.CTkEntry(
            container3,
            placeholder_text='Data'
        )
        self.date.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container3,
            text=','
        )
        label.pack(side=customtkinter.LEFT)

        container4 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container4.pack(fill=customtkinter.BOTH, pady=(0, 15))
        label = customtkinter.CTkLabel(
            container4,
            text='apresentada no espelho de ponto de'
        )
        label.pack(side=customtkinter.LEFT)
        self.mounth = customtkinter.CTkEntry(
            container4,
            placeholder_text='Mês'
        )
        self.mounth.pack(side=customtkinter.LEFT, padx=5)
        label = customtkinter.CTkLabel(
            container4,
            text='de'
        )
        label.pack(side=customtkinter.LEFT)
        self.year = customtkinter.CTkEntry(
            container4,
            placeholder_text='Ano'
        )
        self.year.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container4,
            text='.'
        )
        label.pack(side=customtkinter.LEFT)

        write = ShowWrite(Content, self.data)
        write.pack(fill=customtkinter.BOTH)

        Panel = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        Panel.pack(fill=customtkinter.BOTH, pady=(20, 10))

        panel1 = customtkinter.CTkFrame(Panel, fg_color=("transparent"))
        panel1.pack(pady=(0, 5))
        optionmenu = customtkinter.CTkOptionMenu(
            panel1,
            values=self.values,
            command=self.optionmenu_callback,
            fg_color=('#43434A'),
            button_color=('#2E2E33')
        )
        optionmenu.pack(side=customtkinter.LEFT)
        self.title = customtkinter.CTkEntry(
            panel1,
            placeholder_text='Titulo'
        )
        self.title.pack(side=customtkinter.LEFT, padx=5)
        self.email_us = customtkinter.CTkEntry(
            panel1,
            placeholder_text='Email'
        )
        self.email_us.pack(side=customtkinter.LEFT)

        panel2 = customtkinter.CTkFrame(Panel, fg_color=("transparent"))
        panel2.pack()
        btn = customtkinter.CTkButton(
            panel2, 
            text='Enviar', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=lambda: self.Commit(1)
        )
        btn.pack(side=customtkinter.LEFT)
        self.status = customtkinter.CTkLabel(
            panel2,
            text='...'
        )
        self.status.pack(side=customtkinter.LEFT, padx=5)

    def Registro(self):
        global Content
        if Content:
            Content.destroy()
        Content = customtkinter.CTkFrame(self, fg_color=("transparent"))
        Content.pack(fill=customtkinter.BOTH)

        container1 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container1.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container1,
            text='De ordem do Excelentíssimo Diretor Geral, conforme o procedimento'
        )
        label.pack(side=customtkinter.LEFT)
        self.procedure = customtkinter.CTkEntry(
            container1,
            placeholder_text='Procedimento'
        )
        self.procedure.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container1,
            text=','
        )
        label.pack(side=customtkinter.LEFT)
        
        container2 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container2.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container2,
            text='vimos muito respeitosamente notificar Vossa Senhoria para apresentação de'
        )
        label.pack(side=customtkinter.LEFT)

        container3 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container3.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container3,
            text='justificativa quanto AO REGISTRO ÚNICO na data de'
        )
        label.pack(side=customtkinter.LEFT)
        self.registers = customtkinter.CTkEntry(
            container3,
            placeholder_text='Registro'
        )
        self.registers.pack(side=customtkinter.LEFT, padx=5)
        label = customtkinter.CTkLabel(
            container3,
            text='-'
        )
        label.pack(side=customtkinter.LEFT)

        container4 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container4.pack(fill=customtkinter.BOTH)
        self.hour = customtkinter.CTkEntry(
            container4,
            placeholder_text='Horário'
        )
        self.hour.pack(side=customtkinter.LEFT, padx=0)
        label = customtkinter.CTkLabel(
            container4,
            text=', apresentada no espelho de ponto de'
        )
        label.pack(side=customtkinter.LEFT)
        self.mounth = customtkinter.CTkEntry(
            container4,
            placeholder_text='Mês'
        )
        self.mounth.pack(side=customtkinter.LEFT, padx=(5, 0))

        container5 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container5.pack(fill=customtkinter.BOTH, pady=(0, 15))
        label = customtkinter.CTkLabel(
            container5,
            text='de'
        )
        label.pack(side=customtkinter.LEFT)
        self.year = customtkinter.CTkEntry(
            container5,
            placeholder_text='Ano'
        )
        self.year.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container5,
            text='.'
        )
        label.pack(side=customtkinter.LEFT)

        write = ShowWrite(Content, self.data)
        write.pack(fill=customtkinter.BOTH)

        Panel = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        Panel.pack(fill=customtkinter.BOTH, pady=(20, 10))

        panel1 = customtkinter.CTkFrame(Panel, fg_color=("transparent"))
        panel1.pack(pady=(0, 5))
        optionmenu = customtkinter.CTkOptionMenu(
            panel1,
            values=self.values,
            command=self.optionmenu_callback,
            fg_color=('#43434A'),
            button_color=('#2E2E33')
        )
        optionmenu.pack(side=customtkinter.LEFT)
        self.title = customtkinter.CTkEntry(
            panel1,
            placeholder_text='Titulo'
        )
        self.title.pack(side=customtkinter.LEFT, padx=5)
        self.email_us = customtkinter.CTkEntry(
            panel1,
            placeholder_text='Email'
        )
        self.email_us.pack(side=customtkinter.LEFT)

        panel2 = customtkinter.CTkFrame(Panel, fg_color=("transparent"))
        panel2.pack()
        btn = customtkinter.CTkButton(
            panel2, 
            text='Enviar', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=lambda: self.Commit(2)
        )
        btn.pack(side=customtkinter.LEFT)
        self.status = customtkinter.CTkLabel(
            panel2,
            text='...'
        )
        self.status.pack(side=customtkinter.LEFT, padx=5)
    
    def Insuficiencia(self):
        global Content
        if Content:
            Content.destroy()
        Content = customtkinter.CTkFrame(self, fg_color=("transparent"))
        Content.pack(fill=customtkinter.BOTH)

        container1 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container1.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container1,
            text='De ordem do Excelentíssimo Diretor Geral, conforme o procedimento'
        )
        label.pack(side=customtkinter.LEFT)
        self.procedure = customtkinter.CTkEntry(
            container1,
            placeholder_text='Procedimento'
        )
        self.procedure.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container1,
            text=','
        )
        label.pack(side=customtkinter.LEFT)
        
        container2 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container2.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container2,
            text='vimos muito respeitosamente notificar Vossa Senhoria para apresentação de'
        )
        label.pack(side=customtkinter.LEFT)
        
        container3 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container3.pack(fill=customtkinter.BOTH)
        label = customtkinter.CTkLabel(
            container3,
            text='justificativa quanto À CARGA HORÁRIA INSUFICIENTE no total de'
        )
        label.pack(side=customtkinter.LEFT)
        self.str = customtkinter.CTkEntry(
            container3,
            placeholder_text='Carga Horária'
        )
        self.str.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container3,
            text=','
        )
        label.pack(side=customtkinter.LEFT)

        container4 = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        container4.pack(fill=customtkinter.BOTH, pady=(0, 15))
        label = customtkinter.CTkLabel(
            container4,
            text='apresentada no espelho de ponto de'
        )
        label.pack(side=customtkinter.LEFT)
        self.mounth = customtkinter.CTkEntry(
            container4,
            placeholder_text='Mês'
        )
        self.mounth.pack(side=customtkinter.LEFT, padx=5)
        label = customtkinter.CTkLabel(
            container4,
            text='de'
        )
        label.pack(side=customtkinter.LEFT)
        self.year = customtkinter.CTkEntry(
            container4,
            placeholder_text='Ano'
        )
        self.year.pack(side=customtkinter.LEFT, padx=(5, 0))
        label = customtkinter.CTkLabel(
            container4,
            text='.'
        )
        label.pack(side=customtkinter.LEFT)

        write = ShowWrite(Content, self.data)
        write.pack(fill=customtkinter.BOTH)

        Panel = customtkinter.CTkFrame(Content, fg_color=("transparent"))
        Panel.pack(fill=customtkinter.BOTH, pady=(20, 10))

        panel1 = customtkinter.CTkFrame(Panel, fg_color=("transparent"))
        panel1.pack(pady=(0, 5))
        optionmenu = customtkinter.CTkOptionMenu(
            panel1,
            values=self.values,
            command=self.optionmenu_callback,
            fg_color=('#43434A'),
            button_color=('#2E2E33')
        )
        optionmenu.pack(side=customtkinter.LEFT)
        self.title = customtkinter.CTkEntry(
            panel1,
            placeholder_text='Titulo'
        )
        self.title.pack(side=customtkinter.LEFT, padx=5)
        self.email_us = customtkinter.CTkEntry(
            panel1,
            placeholder_text='Email'
        )
        self.email_us.pack(side=customtkinter.LEFT)

        panel2 = customtkinter.CTkFrame(Panel, fg_color=("transparent"))
        panel2.pack()
        btn = customtkinter.CTkButton(
            panel2, 
            text='Enviar', 
            fg_color=('#43434A'), 
            hover_color=('#2E2E33'),
            command=lambda: self.Commit(3)
        )
        btn.pack(side=customtkinter.LEFT)
        self.status = customtkinter.CTkLabel(
            panel2,
            text='...'
        )
        self.status.pack(side=customtkinter.LEFT, padx=5)

    def optionmenu_callback(self, choice):
        self.selected_email = choice

    def Commit(self, id):
        if hasattr(self, 'selected_email'):
            procedure = self.procedure.get()
            mounth = self.mounth.get()
            year = self.year.get()
            title = self.title.get()
            email_us = self.email_us.get()
            match id:
                case 1:
                    date = self.date.get()
                    status = PontoExtend.Ausencia(
                        self.selected_email,
                        procedure,
                        mounth,
                        year,
                        title,
                        date,
                        email_us,
                        self.data.nome,
                        self.data.cargo
                    )
                    if status:
                        self.status.configure(text=status)
                case 2:
                    register = self.registers.get()
                    hour = self.hour.get()
                    status = PontoExtend.Unico(
                       self.selected_email,
                        procedure,
                        mounth,
                        year,
                        title,
                        register,
                        hour,
                        email_us,
                        self.data.nome,
                        self.data.cargo 
                    )
                    if status:
                        self.status.configure(text=status)
                case 3:
                    str = self.str.get()
                    status = PontoExtend.Insuficiente(
                       self.selected_email,
                        procedure,
                        mounth,
                        year,
                        title,
                        str,
                        email_us,
                        self.data.nome,
                        self.data.cargo 
                    )
                    if status:
                        self.status.configure(text=status)