from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    percentage = models.IntegerField(default=False)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=55)
    detail = models.CharField(max_length=180)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)

    def __str__(self):
        return self.title