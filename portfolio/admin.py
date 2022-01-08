from django.contrib import admin
from .models import *

# Register your models here.
myModels = [Project, Skill, Service]
admin.site.register(myModels)