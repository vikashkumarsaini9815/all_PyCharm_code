from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name