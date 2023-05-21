import smtplib
import ssl
import os


def send_email(receiver, message):
    host = "smtp.gmail.com"
    port = 465

    username = "costinbogdan145@gmail.com"
    password = os.getenv("PASS")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
