from django.shortcuts import render
from email.message import EmailMessage
import ssl
import smtplib
from .forms import InfoFromUser
from .models import UserInformation
from django.template.loader import get_template
import imaplib
import email
from email.header import decode_header
import os


def home_page(request):
    return render(request, "home.html")

def WriteMail(request):
    content ={}
    content['form']= InfoFromUser()
    #email_sender = ''
    #email_reciver = ''
    #subject = ''
    #body = ''

    if request.method == "POST":

        email_sender = request.POST['user_email']
        email_password = 'dbbkbvajkdgcrygf'

        email_reciver = request.POST['reciver_email']

        subject = request.POST['title']
        body = request.POST['mail_content']

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciver, em.as_string())

    return render(request, "write.html", content)


def AllSendedMail(request):
    
    return render(request, 'sended.html')

