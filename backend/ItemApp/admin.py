from django.contrib import admin

# Register your models here.

from django.contrib.admin.options import ModelAdmin
from . import models


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',
                    'date', 'category', 'title', 'value']


admin.site.register(models.Items, ItemsAdmin)
