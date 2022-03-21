from django.db import models

# Create your models here.

class User(models.Model) :
    name = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=10, blank=True, unique=True)
    email = models.EmailField()
    parent_contact = models.CharField(max_length=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return f'{self.name},{self.contact}'

class Level(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, null=True, blank=True)
    level_name = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='level_image', null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    components = models.CharField(max_length=255, null=True, blank=True)
    key_concept = models.CharField(max_length=255, null=True, blank=True)
    key_skills = models.CharField(max_length=255, null=True, blank=True)
    kit = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self) :
        return self.level_name

class Challenge(models.Model) :
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    challenge_name = models.CharField(max_length=20, null=True, blank=True)
    problem_statement = models.CharField(max_length=255, null=True, blank=True)
    Rules = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='challenge_image',null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    document = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self) :
        return self.challenge_name

class Media(models.Model) :
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    media_name = models.CharField(max_length=20, null=True, blank=True)
    media_type = models.CharField(max_length=50, null=True, blank=True)
    media_path = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self) :
        return self.media_name