from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import datetime as dt 


# Create your models here.
class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()
