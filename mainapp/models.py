from django.db import models


# Create your models here.
class NameModel(models.Model):
    name = models.CharField('Name', max_length=50)
    age = models.PositiveIntegerField(max_length=3)