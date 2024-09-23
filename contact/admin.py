from django.contrib import admin
from . import models 
# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name','email']
admin.site.register(models.Contact_us,ContactModelAdmin)
