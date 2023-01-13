from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(min_length=1, max_length=200)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]