from django.db import models
from django.urls import reverse


# Create your models here.
class NameModel(models.Model):
    name = models.CharField('Name', max_length=50)
    age = models.PositiveIntegerField('Age')

    def get_absolute_url(self):
        return reverse("mainapp:update", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'

        def __str__(self):
            return self.name
