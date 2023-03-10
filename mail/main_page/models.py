from django.db import models
from django.contrib.auth.models import User

class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userinformation", null=True)
    user_email = models.CharField(max_length=100)
    reciver_email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    mail_content = models.CharField(max_length=1000)


class RecivedInformation(models.Model):
    recived_subject = models.CharField(max_length=100)
    recived_from = models.CharField(max_length=100)
    recived_content = models.CharField(max_length=5000)
    
