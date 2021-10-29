from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Profile)

@admin.register(User_Profile)
class User_profile(admin.ModelAdmin):
    list_display = ('user','about', 'phone', 'city', 'state', 'country')