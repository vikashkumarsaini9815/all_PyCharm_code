from rest_framework import serializers
from .models import Games, Student, Level, Challenge, Media




class StudentSerializer(serializers.ModelSerializer):    
    class Meta:
         model = Student
         fields = ['id', 'name', 'photo', 'contact', 'email', 'parent_contact']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class ChallengeSerializer(serializers.ModelSerializer):
    medias=MediaSerializer(many=True, read_only=True)
    class Meta:
        model = Challenge
        fields = '__all__'



class LevelSerializer(serializers.ModelSerializer):
    challenges=ChallengeSerializer(many=True, read_only=True)
    class Meta:
        model = Level
        fields = '__all__'

class LeveldactiveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Level
        fields = ['id', 'level_number', 'level_name', 'photo']


class GamesSerializer(serializers.ModelSerializer):
    levels = LevelSerializer(many=True, read_only=True)
    class Meta:
        model = Games
        fields = "__all__"


class StudentsSerializer(serializers.ModelSerializer):
    game = GamesSerializer(many=True, read_only=True)    
    class Meta:
        model = Student
        fields = ['id', 'name', 'photo', 'contact', 'email', 'parent_contact', 'game', 'level', 'challenge']
       # fields = '__all__'

class Games3Serializer(serializers.ModelSerializer):
   # levels = LevelSerializer(many=True, read_only=True)    
    class Meta:
        model = Games
        fields = ['game_name', 'game_type', 'gamephoto']
       # fields = '__all__'