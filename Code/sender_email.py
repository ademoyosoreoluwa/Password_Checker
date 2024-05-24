# Send Email Code

import smtplib
from email.message import EmailMessage


email_address = 'abcdef@gmail.com'
password = 'abcd12345'


to_email = 'gnbvcfdre@hotmail.com'
email_body = 'I am a python learner!'
email_subject = 'Testing From Python!'

msg = EmailMessage()
msg['From'] = 'New Coder'
msg['To'] = to_email
msg['Subject'] = email_subject
msg.set_content(email_body)

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_address, password)
        smtp.send_message(msg)
        print('Email sent successfully!!!')
except smtplib.SMTPAuthenticationError as err:
    print(f"Failed to authenticate: {err}")
except Exception as err:
    print(f"An error occurred: {err}")



# Sending customize email

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


email_address = 'abcdef@gmail.com'
password = 'abcd12345'

html = Template(Path('index.html').read_text())
to_email = 'gnbvcfdre@hotmail.com'
email_body = 'I am a python learner!'
email_subject = 'Testing From Python!'

msg = EmailMessage()
msg['From'] = 'New Coder'
msg['To'] = to_email
msg['Subject'] = email_subject
msg.set_content(html.substitute({'name': 'TinTin'}, 'html')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_address, password)
        smtp.send_message(msg)
        print('Email sent successfully!!!')
except smtplib.SMTPAuthenticationError as err:
    print(f"Failed to authenticate: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
