from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('write/', views.WriteMail, name='WriteMail'),
    path('sended/', views.AllSendedMail, name='AllSendedMail'),
    path('', views.home_page, name='HomePage')
]