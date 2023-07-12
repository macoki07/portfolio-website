from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from markdownx.models import MarkdownxField

class User(AbstractUser):
    pass

class Profile(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="profile/") 
    mission = models.CharField(max_length=75)
    about = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}'s Profile"

class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    priority = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Section {self.title}"
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    media = models.FileField(upload_to="projects/")
    details = models.TextField(max_length=4096)
    priority = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Project {self.title}"

