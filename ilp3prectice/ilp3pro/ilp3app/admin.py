from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display= ['name','contact','email','parent_contact']
    search_fields = ['name',]
admin.site.register(Student, StudentAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display = ['level_number','level_name','description','photo']
    search_fields = ['level_number',]
admin.site.register(Level, LevelAdmin)

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['challenge_name','description','document','video_link','photo']
    search_fields = ['challenge_name']
admin.site.register(Challenge, ChallengeAdmin)

class MediaAdmin(admin.ModelAdmin):
    list_display = ['challenge','media_name','media_type','media_path']
    search_fields = ['media_name']
admin.site.register(Media, MediaAdmin)


class GamesAdmin(admin.ModelAdmin):
    list_display = ['game_name','price','age_group',]
admin.site.register(Games,GamesAdmin)