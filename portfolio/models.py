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