import email.message
import smtplib
import json

from app.model.email.EmailSearch import EmailPassword

def EmailPontoEnviar(title, assinatura, cargo, procedimento, email_selecionado):
    senha = [s for x in EmailPassword(email_selecionado) for s in x][0]

    with open('app/config/json/epth.json', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        if item["Data"] not in ['nan', 'NaT']:
            body = f'''
            <p style="text-align: justify;">
                De ordem do Excelentíssimo Diretor Geral, conforme o procedimento {procedimento}, vimos muito respeitosamente notificar Vossa Senhoria para
                apresentação de justificativa quanto <strong>À AUSÊNCIA DE REGISTRO</strong> na data de 
                {item["Data"]}, apresentada no espelho de ponto de <strong>{item["Mês"]}</strong> de {item["Ano"]}.
            </p> 
            <p style="text-align: justify;">
                Informo que a <strong>justificativa deve ser encaminhada contendo ciência da chefia imediata</strong>, e ser pautada em  
                algumas das hipóteses previstas na RESOLUÇÃO Nº 037/2022/DPG. Em caso de não apresentação da 
                justificativa, <strong>será realizado o desconto proporcional nos vencimentos</strong>.
            </p>
            <p style="text-align: justify;">
                Sendo assim, fica estabelecido <strong>prazo de 5 (cinco)</strong> dias úteis para apresentação da justificativa, que deverá ser 
                encaminhada como resposta a este e-mail.
            </p>
            <p style="text-align: justify; margin-bottom: 50px;">
                Caso tenha aberto o procedimento anterior à notificação para justificar a inadimplência, informar seu 
                respectivo número. Entretanto, após a notificação da irregularidade, a justificativa deverá ser 
                encaminhada em resposta ao e-mail <span style="font-weight: bold; text-decoration: underline;">SEM</span> abertura de novo procedimento. 
            </p>
            <p style="text-align: justify; text-decoration: underline; font-weight: bold; background: yellow; margin-bottom: 20px;">
                AS MANIFESTAÇÕES DEVEM SER ACOMPANHADAS DA CIÊNCIA DA CHEFIA IMEDIATA EM RESPOSTA A ESSE E-MAIL.
            </p>
            <p>
                Ficamos à disposição para eventuais esclarecimentos.
            </p>
            <p>
                Respeitosamente, <br>
                {assinatura} <br>
                {cargo}
            </p>    
            '''

            msg = email.message.Message()
            msg['Subject'] = f'{title}'
            msg['From'] = f'{email_selecionado}'
            msg['To'] = f'{item["EMAIL"]}' 
            password = f'{senha}'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

        if item["Registro Ímpar"] not in ['nan']:
            body = f'''
            <p style="text-align: justify;">
                De ordem do Excelentíssimo Diretor Geral, conforme o procedimento {procedimento}, vimos muito respeitosamente notificar Vossa Senhoria para  
                apresentação de justificativa quanto <strong>AO REGISTRO ÚNICO</strong> na data  
                de {item["Registro Ímpar"]} - {item["Horário"]}, apresentada no espelho de ponto de <strong>{item["Mês"]}</strong> de {item["Ano"]}.
            </p> 
            <p style="text-align: justify;">
                Informo que a <strong>justificativa deve ser encaminhada contendo ciência da chefia imediata</strong>, e ser pautada em  
                algumas das hipóteses previstas na RESOLUÇÃO Nº 037/2022/DPG. Em caso de não apresentação da 
                justificativa, <strong>será realizado o desconto proporcional nos vencimentos</strong>.
            </p>
            <p style="text-align: justify;">
                Sendo assim, fica estabelecido <strong>prazo de 5 (cinco)</strong> dias úteis para apresentação da justificativa, que deverá ser 
                encaminhada como resposta a este e-mail.
            </p>
            <p style="text-align: justify; margin-bottom: 50px;">
                Caso tenha aberto o procedimento anterior à notificação para justificar a inadimplência, informar seu 
                respectivo número. Entretanto, após a notificação da irregularidade, a justificativa deverá ser 
                encaminhada em resposta ao e-mail <span style="font-weight: bold; text-decoration: underline;">SEM</span> abertura de novo procedimento. 
            </p>
            <p style="text-align: justify; text-decoration: underline; font-weight: bold; background: yellow; margin-bottom: 20px;">
                AS MANIFESTAÇÕES DEVEM SER ACOMPANHADAS DA CIÊNCIA DA CHEFIA IMEDIATA EM RESPOSTA A ESSE E-MAIL.
            </p>
            <p>
                Ficamos à disposição para eventuais esclarecimentos.
            </p>
            <p>
                Respeitosamente, <br>
                {assinatura} <br>
                {cargo}
            </p>
            '''

            msg = email.message.Message()
            msg['Subject'] = f'{title}'
            msg['From'] = f'{email_selecionado}'
            msg['To'] = f'{item["EMAIL"]}' 
            password = f'{senha}'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

        if item["Carga Horária Insuficiente"] not in ['nan']:
            body = f'''
            <p style="text-align: justify;">
                De ordem do Excelentíssimo Diretor Geral, conforme o procedimento {procedimento}, vimos muito respeitosamente notificar Vossa Senhoria para  
                apresentação de justificativa quanto <strong>À CARGA HORÁRIA INSUFICIENTE</strong> no total  
                de {item["Carga Horária Insuficiente"]}, apresentada no espelho de ponto de <strong>{item["Mês"]}</strong> de {item["Ano"]}.
            </p> 
            <p style="text-align: justify;">
                Informo que a <strong>justificativa deve ser encaminhada contendo ciência da chefia imediata</strong>, e ser pautada em  
                algumas das hipóteses previstas na RESOLUÇÃO Nº 037/2022/DPG. Em caso de não apresentação da 
                justificativa, <strong>será realizado o desconto proporcional nos vencimentos</strong>.
            </p>
            <p style="text-align: justify;">
                Sendo assim, fica estabelecido <strong>prazo de 5 (cinco)</strong> dias úteis para apresentação da justificativa, que deverá ser 
                encaminhada como resposta a este e-mail.
            </p>
            <p style="text-align: justify; margin-bottom: 50px;">
                Caso tenha aberto o procedimento anterior à notificação para justificar a inadimplência, informar seu 
                respectivo número. Entretanto, após a notificação da irregularidade, a justificativa deverá ser 
                encaminhada em resposta ao e-mail <span style="font-weight: bold; text-decoration: underline;">SEM</span> abertura de novo procedimento. 
            </p>
            <p style="text-align: justify; text-decoration: underline; font-weight: bold; background: yellow; margin-bottom: 20px;">
                AS MANIFESTAÇÕES DEVEM SER ACOMPANHADAS DA CIÊNCIA DA CHEFIA IMEDIATA EM RESPOSTA A ESSE E-MAIL.
            </p>
            <p>
                Ficamos à disposição para eventuais esclarecimentos.
            </p>
            <p>
                Respeitosamente, <br>
                {assinatura} <br>
                {cargo}
            </p>
            '''

            msg = email.message.Message()
            msg['Subject'] = f'{title}'
            msg['From'] = f'{email_selecionado}'
            msg['To'] = f'{item["EMAIL"]}' 
            password = f'{senha}'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

class PontoExtend:
    def Ausencia(email_selected, procedure, mounth, year, title, date, email_us, signature, office):
        try:
            passw = [s for x in EmailPassword(email_selected) for s in x][0]

            body = f'''
            <p style="text-align: justify;">
                De ordem do Excelentíssimo Diretor Geral, conforme o procedimento {procedure}, vimos muito respeitosamente notificar Vossa Senhoria para
                apresentação de justificativa quanto <strong>À AUSÊNCIA DE REGISTRO</strong> na data de 
                {date}, apresentada no espelho de ponto de <strong>{mounth}</strong> de {year}.
            </p> 
            <p style="text-align: justify;">
                Informo que a <strong>justificativa deve ser encaminhada contendo ciência da chefia imediata</strong>, e ser pautada em  
                algumas das hipóteses previstas na RESOLUÇÃO Nº 037/2022/DPG. Em caso de não apresentação da 
                justificativa, <strong>será realizado o desconto proporcional nos vencimentos</strong>.
            </p>
            <p style="text-align: justify;">
                Sendo assim, fica estabelecido <strong>prazo de 5 (cinco)</strong> dias úteis para apresentação da justificativa, que deverá ser 
                encaminhada como resposta a este e-mail.
            </p>
            <p style="text-align: justify; margin-bottom: 50px;">
                Caso tenha aberto o procedimento anterior à notificação para justificar a inadimplência, informar seu 
                respectivo número. Entretanto, após a notificação da irregularidade, a justificativa deverá ser 
                encaminhada em resposta ao e-mail <span style="font-weight: bold; text-decoration: underline;">SEM</span> abertura de novo procedimento. 
            </p>
            <p style="text-align: justify; text-decoration: underline; font-weight: bold; background: yellow; margin-bottom: 20px;">
                AS MANIFESTAÇÕES DEVEM SER ACOMPANHADAS DA CIÊNCIA DA CHEFIA IMEDIATA EM RESPOSTA A ESSE E-MAIL.
            </p>
            <p>
                Ficamos à disposição para eventuais esclarecimentos.
            </p>
            <p>
                Respeitosamente, <br>
                {signature} <br>
                {office}
            </p>    
            '''

            msg = email.message.Message()
            msg['Subject'] = f'{title}'
            msg['From'] = f'{email_selected}'
            msg['To'] = f'{email_us}' 
            password = f'{passw}'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

            rtn = f'Enviado -> {email_us}'
        except Exception as e:
            rtn = e
            
        return rtn

    def Unico(email_selected, procedure, mounth, year, title, register, hour, email_us, signature, office):
        try:
            passw = [s for x in EmailPassword(email_selected) for s in x][0]

            body = f'''
            <p style="text-align: justify;">
                De ordem do Excelentíssimo Diretor Geral, conforme o procedimento {procedure}, vimos muito respeitosamente notificar Vossa Senhoria para  
                apresentação de justificativa quanto <strong>AO REGISTRO ÚNICO</strong> na data  
                de {register} - {hour}, apresentada no espelho de ponto de <strong>{mounth}</strong> de {year}.
            </p> 
            <p style="text-align: justify;">
                Informo que a <strong>justificativa deve ser encaminhada contendo ciência da chefia imediata</strong>, e ser pautada em  
                algumas das hipóteses previstas na RESOLUÇÃO Nº 037/2022/DPG. Em caso de não apresentação da 
                justificativa, <strong>será realizado o desconto proporcional nos vencimentos</strong>.
            </p>
            <p style="text-align: justify;">
                Sendo assim, fica estabelecido <strong>prazo de 5 (cinco)</strong> dias úteis para apresentação da justificativa, que deverá ser 
                encaminhada como resposta a este e-mail.
            </p>
            <p style="text-align: justify; margin-bottom: 50px;">
                Caso tenha aberto o procedimento anterior à notificação para justificar a inadimplência, informar seu 
                respectivo número. Entretanto, após a notificação da irregularidade, a justificativa deverá ser 
                encaminhada em resposta ao e-mail <span style="font-weight: bold; text-decoration: underline;">SEM</span> abertura de novo procedimento. 
            </p>
            <p style="text-align: justify; text-decoration: underline; font-weight: bold; background: yellow; margin-bottom: 20px;">
                AS MANIFESTAÇÕES DEVEM SER ACOMPANHADAS DA CIÊNCIA DA CHEFIA IMEDIATA EM RESPOSTA A ESSE E-MAIL.
            </p>
            <p>
                Ficamos à disposição para eventuais esclarecimentos.
            </p>
            <p>
                Respeitosamente, <br>
                {signature} <br>
                {office}
            </p>
            '''

            msg = email.message.Message()
            msg['Subject'] = f'{title}'
            msg['From'] = f'{email_selected}'
            msg['To'] = f'{email_us}' 
            password = f'{passw}'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

            rtn = f'Enviado -> {email_us}'
        except Exception as e:
            rtn = e
            
        return rtn

    def Insuficiente(email_selected, procedure, mounth, year, title, str, email_us, signature, office):
        try:
            passw = [s for x in EmailPassword(email_selected) for s in x][0]

            body = f'''
            <p style="text-align: justify;">
                De ordem do Excelentíssimo Diretor Geral, conforme o procedimento {procedure}, vimos muito respeitosamente notificar Vossa Senhoria para  
                apresentação de justificativa quanto <strong>À CARGA HORÁRIA INSUFICIENTE</strong> no total  
                de {str}, apresentada no espelho de ponto de <strong>{mounth}</strong> de {year}.
            </p> 
            <p style="text-align: justify;">
                Informo que a <strong>justificativa deve ser encaminhada contendo ciência da chefia imediata</strong>, e ser pautada em  
                algumas das hipóteses previstas na RESOLUÇÃO Nº 037/2022/DPG. Em caso de não apresentação da 
                justificativa, <strong>será realizado o desconto proporcional nos vencimentos</strong>.
            </p>
            <p style="text-align: justify;">
                Sendo assim, fica estabelecido <strong>prazo de 5 (cinco)</strong> dias úteis para apresentação da justificativa, que deverá ser 
                encaminhada como resposta a este e-mail.
            </p>
            <p style="text-align: justify; margin-bottom: 50px;">
                Caso tenha aberto o procedimento anterior à notificação para justificar a inadimplência, informar seu 
                respectivo número. Entretanto, após a notificação da irregularidade, a justificativa deverá ser 
                encaminhada em resposta ao e-mail <span style="font-weight: bold; text-decoration: underline;">SEM</span> abertura de novo procedimento. 
            </p>
            <p style="text-align: justify; text-decoration: underline; font-weight: bold; background: yellow; margin-bottom: 20px;">
                AS MANIFESTAÇÕES DEVEM SER ACOMPANHADAS DA CIÊNCIA DA CHEFIA IMEDIATA EM RESPOSTA A ESSE E-MAIL.
            </p>
            <p>
                Ficamos à disposição para eventuais esclarecimentos.
            </p>
            <p>
                Respeitosamente, <br>
                {signature} <br>
                {office}
            </p>
            '''

            msg = email.message.Message()
            msg['Subject'] = f'{title}'
            msg['From'] = f'{email_selected}'
            msg['To'] = f'{email_us}' 
            password = f'{passw}'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

            rtn = f'Enviado -> {email_us}'
        except Exception as e:
            rtn = e
            
        return rtn