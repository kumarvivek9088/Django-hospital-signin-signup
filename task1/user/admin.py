from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Doctor,Patient,User
# Register your models here.
admin.site.register(Doctor)
admin.site.register(User,UserAdmin)
admin.site.register(Patient)

