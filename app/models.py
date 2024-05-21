from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.ManyToManyField(Skill, related_name='projects')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images')


