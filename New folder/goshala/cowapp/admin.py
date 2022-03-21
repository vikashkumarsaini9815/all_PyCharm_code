from django.contrib import admin
from .models import Contactus
# Register your models here.
class ContactusAdmin(admin.ModelAdmin):
    list_display= ['name','contact','email','message']
    search_fields = ['contact',]
admin.site.register(Contactus, ContactusAdmin)