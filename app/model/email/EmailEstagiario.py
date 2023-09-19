import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from app.model.email.EmailSearch import EmailPassword

def EmailEstagiarios(email_select, emails, nome, data, assinatura, cargo, resolucao, arquivo):
    senha = [s for x in EmailPassword(email_select) for s in x][0]
    for em in emails:
        body = f'''
            <p>
                <strong>Exmo. (a) Defensor (a) Público (a),</strong>
            </p>
            <br>
            <p style="text-align: justify;">
                Comunico, por meio deste, que o (a) estagiário (a) 
                <strong>{nome}</strong> encontra-se 
                <span style="background: yellow;"><strong>CONTRATADO (A)</strong></span>, 
                conforme solicitado no Processo <strong>Nº {resolucao}</strong>.  
                Desta feita, informo que o (a) supracitado (a) estagiário (a) está autorizado (a) a 
                iniciar suas atividades no dia  <span style="background: yellow;"><strong>{data}</strong></span> sob vossa supervisão.
            </p>
            <br>
            <p>
                Anexo termo de compromisso assinado.
            </p>
            <br>
            <p>
                Respeitosamente,
            </p>
            <br>
            <p>
                {assinatura} <br>
                {cargo} <br>
                <strong>
                    Coordenadoria de Gestão Funcional <br>
                    Defensoria Pública do Estado de Mato Grosso <br>
                    (65) 99954-5349
                </strong>
            </p>
        '''

        msg = MIMEMultipart()
        msg['Subject'] = f'CIÊNCIA DA CONTRATAÇÃO - {resolucao} - ESTAGIÁRIO {nome}'
        msg['From'] = f'{email_select}'
        msg['To'] = f'{em}'
        msg.attach(MIMEText(body, 'html'))
        if len(arquivo) > 0:
            for file in arquivo:
                filename = file.split("/")[-1]
                with open(file, "rb") as pdf_file:
                    attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
                    attachment.add_header("Content-Disposition", f"attachment; filename={filename}")
                    msg.attach(attachment)
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        password = f'{senha}'
        s.login(msg['From'], password)
        s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))