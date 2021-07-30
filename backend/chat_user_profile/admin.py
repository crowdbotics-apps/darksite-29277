from django.contrib import admin
from .models import Profile, Contact, VerificationCode

admin.site.register(VerificationCode)
admin.site.register(Contact)
admin.site.register(Profile)

# Register your models here.