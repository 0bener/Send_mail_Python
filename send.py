#importar modulos necessários
import os
import smtplib
from email.message import EmailMessage

#configurar e-mail e senha
EMAIL_ADDRESS = 'seuemail@domain.com'
EMAIL_PASSWORD = 'suasenha↑'

#criar e-mail
msg = EmailMessage()
msg['Subject'] = 'Titulo da Msg'
msg['From'] = 'email@origem↑'
msg['To']= 'email@destino'
msg.set_content('Mensagem que será enviada.')

#enviar emial
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
