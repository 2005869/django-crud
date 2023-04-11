from django.db import models


# Create your models here.
class NameModel(models.Model):
    name = models.CharField('Name', max_length=50)
    age = models.PositiveIntegerField('Age')

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'

        def __str__(self):
            return self.name

