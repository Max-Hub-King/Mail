from django.shortcuts import render
from email.message import EmailMessage
import ssl
import smtplib
from .forms import InfoFromUser, InfoFromRecivedUser
from .models import UserInformation, RecivedInformation
from django.template.loader import get_template
import imaplib
import email
from email.header import decode_header
from register.forms import RegisterForm


def home_page(request):
    return render(request, "home.html")

def WriteMail(request):
    content ={}
    content['form']= InfoFromUser()

    if request.method == "POST":

        email_sender = request.POST.get['email']
        email_password = ''

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
    imap_server = 'imap.gmail.com'
    email_address = ''
    password = ''
    content_from = []
    content_title = []
    content_body = []

    imap = imaplib.IMAP4_SSL(imap_server, port=993)

    imap.login(email_address, password)

    status, message = imap.select("Inbox")

    numOfMessages = int(message[0])

    def obtain_header(msg):
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding='utf-8')

        From, encoding = decode_header(msg.get("From"))[0]
        if isinstance(From, bytes):
            From = From.decode(encoding='utf-8')
        
        return subject, From

    for i in range(numOfMessages, numOfMessages - 4, -1):
        information = ''
        res, msg = imap.fetch(str(i), "(RFC822)")  # fetches the email using it's ID

        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, From = obtain_header(msg)
                content_from.append(From)
                content_title.append(subject)
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        try: body = part.get_payload(decode=True).decode()
                        except: pass
                        if content_type == "text/plain":
                                information += body + "\n"
                    content_body.append(information)
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print(body)
                        content_body.append(body)
        
                
    mycontentlist = zip(content_from, content_title,content_body)
    content_sended = {
        'mycontentlist' : mycontentlist,
            }
    imap.close()
    return render(request, 'sended.html', content_sended)

