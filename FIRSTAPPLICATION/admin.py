from django.contrib import admin
from django.db import models
from . models import User

# Register your models here.
#admin.site.register(User) This line for basic registartion of our model

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']