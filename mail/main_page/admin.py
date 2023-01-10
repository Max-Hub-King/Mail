from django.contrib import admin

from .models import UserInformation, RecivedInformation

# Register your models here.
admin.site.register(UserInformation)
admin.site.register(RecivedInformation)
