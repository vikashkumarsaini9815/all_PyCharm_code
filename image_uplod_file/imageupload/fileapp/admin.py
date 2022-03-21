from django.contrib import admin
from .models import File
# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'remark', 'timestamp')
    search_fields = ['file']
admin.site.register(File, FileAdmin) 