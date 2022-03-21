from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=10, blank=True, unique=True)
    email = models.EmailField()
    parent_contact = models.CharField(max_length=10, null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return f'{self.name},{self.contact}'


# create transactions_details

class Transactions_details(models.Model):
    transactions_id = models.CharField(max_length=255)
    game_id = models.ForeignKey(Student,on_delete=models.CASCADE)


# create jwt authentications model

class Secret(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    jwt_token = models.CharField(max_length=255, null=True, blank=True)
    jwt_timestamp = models.DateTimeField(null=True, blank=True)
    otp_timestamp = models.DateTimeField(null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)

# create games product

class Games(models.Model):
    game_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    mode = models.CharField(max_length=255, null=True, blank=True)
    age_group = models.CharField(max_length=50, null=True, blank=True)
    emi = models.CharField(max_length=255, null=True, blank=True)
    key_skills = models.TextField(null=True, blank=True)
    key_concept = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    game_type = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    membership = models.CharField(max_length=255, null=True, blank=True)
    shipping = models.CharField(max_length=255, null=True, blank=True)
    program = models.TextField(null=True, blank=True)
    discount = models.CharField(max_length=50, null=True, blank=True)
    components = models.TextField(null=True, blank=True)
    learning_projects = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_video_id = models.CharField(max_length=255, null=True, blank=True)
    total_stem_kits = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.game_name

# create game levels

class Level(models.Model):
    level = models.CharField(max_length=20, null=True, blank=True)
    level_name = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='level_image', null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    components = models.CharField(max_length=255, null=True, blank=True)
    key_concept = models.CharField(max_length=255, null=True, blank=True)
    key_skills = models.CharField(max_length=255, null=True, blank=True)
    kit = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='levels')
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return self.level_name

# create challenge in levels

class Challenge(models.Model):
    challenge_name = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='challenge_image', null=True)
    problem_statement = models.CharField(max_length=255, null=True, blank=True)
    Rules = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    document = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.CharField(max_length=100, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='challenges')

    def __str__(self):
        return self.challenge_name

# create media in challenge

class Media(models.Model):
    media_name = models.CharField(max_length=20, null=True, blank=True)
    media_type = models.CharField(max_length=50, null=True, blank=True)
    media_path = models.CharField(max_length=100, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='medias')

    def __str__(self):
        return self.media_name

# create sudent media

class Student_media(models.Model):
    media_name = models.CharField(max_length=255)
    challenge_id = models.ForeignKey(Challenge,on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level,on_delete=models.CASCADE)
    media_path = models.CharField(max_length=255)


#  create student_details models

class Student_details(models.Model):
    level_id = models.IntegerField()
    level_challenge_id = models.IntegerField()
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
