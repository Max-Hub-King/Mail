from django import forms
from .models import UserInformation, RecivedInformation
from register.forms import RegisterForm

class InfoFromUser(forms.ModelForm):
    user_email = forms.EmailField(max_length=100, required=True, label='',
    widget=forms.TextInput(attrs={
        'class': 'user_mail',
        'placeholder': 'From:',
        'name': 'user_mail_name',
    }))
    reciver_email = forms.EmailField(max_length=100, required=True, label='',
    widget=forms.TextInput(attrs={
        'class': 'reciver_mail',
        'placeholder': 'To:',
        'name': 'reciver_mail_name',
    }))
    title = forms.CharField(max_length=100, required=True, label='',
    widget=forms.TextInput(attrs={
        'class': 'title_of_mail',
        'placeholder': 'Title:',
        'name': 'title_mail_name',
    }))
    mail_content = forms.CharField(max_length=10000, required=True, label='',
    widget=forms.Textarea(attrs={
        'class': 'writen_mail',
        'name': 'content_mail_name',
    }))
    class Meta:
        model = UserInformation
        fields = [
            'user_email',
            'reciver_email',
            'title',
            'mail_content',
        ]

class InfoFromRecivedUser(forms.ModelForm):
    recived_subject = forms.CharField(max_length=100,  
    label='Title',
    widget=forms.Textarea(attrs={
        'class': 'recived_subject',
    }))
    recived_from = forms.EmailField(max_length=100,  
    label='From',
    widget=forms.Textarea(attrs={
        'class': 'recived_from',
    }))
    recived_content = forms.CharField(max_length=5000,  
    label='Content',
    widget=forms.Textarea(attrs={
        'class': 'recived_content',
    }))

    class Meta:
        model = RecivedInformation
        fields = [
            'recived_from',
            'recived_subject',
            'recived_content',
        ]

