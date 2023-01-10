from django import forms
from .models import UserInformation, RecivedInformation

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
    recived_subject = forms.EmailField(max_length=100,  label='',
    widget=forms.Textarea(attrs={
        'class': 'recived_subject',
    }))
    recived_from = forms.EmailField(max_length=100,  label='',
    widget=forms.Textarea(attrs={
        'class': 'recived_subject',
    }))
    recived_content = forms.CharField(max_length=100,  label='',
    widget=forms.Textarea(attrs={
        'class': 'recived_subject',
    }))

    class Meta:
        model = RecivedInformation
        fields = [
            'recived_from',
            'recived_subject',
            'recived_content',
        ]

