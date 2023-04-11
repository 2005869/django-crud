from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.NameModel)
class NameAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
