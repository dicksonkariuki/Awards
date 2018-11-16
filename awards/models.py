from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

# Create your models here.
class Categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    class Meta:
        ordering = ['categories']

class Technologies(models.Model):
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return technologies

    class Meta:
        ordering = ['technologies']

class Colors(models.Model):
    colors = models.CharField(max_length=100)

    def __str__(self):
        return colors

    class Meta:
        ordering = ['colors']

class Countries(models.Model):
    countries = models.CharField(max_length=100)

    def __str__(self):
        return colors

    class Meta:
        ordering = ['countries']

class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='landingpage/')
    description = HTMLField()
    link= models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    bio = HTMLField()
    country = models.ForeignKey(Countries,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
