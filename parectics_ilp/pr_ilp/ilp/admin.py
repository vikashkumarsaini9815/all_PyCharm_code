
from django.contrib import admin
from ilp.models import *
# Register your models here.

 

class UserAdmin(admin.ModelAdmin):
    list_display=['name','contact','email','parent_contact','created','updated']
    search_fields = ['name']
admin.site.register(User, UserAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display = ['user','level','level_name','description','kit','photo']
    search_fields = ['level']
admin.site.register(Level, LevelAdmin)

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['level','challenge_name','description','document','video_link','photo']
    search_fields = ['challenge_name']
admin.site.register(Challenge, ChallengeAdmin)

class MediaAdmin(admin.ModelAdmin):
    list_display = ['challenge','media_name','media_type','media_path']
    search_fields = ['media_name']
admin.site.register(Media, MediaAdmin)