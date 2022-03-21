from django.contrib import admin
from .models import *
# Register your models here.

class GamesAdmin(admin.ModelAdmin):
    list_display = ['game_name', 'price','mode','age_group','emi','key_skills','key_concept','title','game_type','description','duration','membership','shipping',
    'program','discount','components','learning_projects','image_url','youtube_video_id','total_stem_kits','created','updated']
    search_fields = ['product_name']
admin.site.register(Games, GamesAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','contact','email','parent_contact','created','updated']
    search_fields = ['name']
admin.site.register(Student, StudentAdmin)

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

class Transactions_detailsAdmin(admin.ModelAdmin):
    list_display = ['transactions_id','game_id']
admin.site.register(Transactions_details,Transactions_detailsAdmin)


class Student_mediaAdmin(admin.ModelAdmin):
    list_display = ['challenge_id','level_id','media_path','media_name']
    search_fields = ['media_name']
admin.site.register(Student_media, Student_mediaAdmin)


class Student_detailsAdmin(admin.ModelAdmin):
    list_display = ['challenge_id','level_id']
admin.site.register(Student_details, Student_detailsAdmin)
