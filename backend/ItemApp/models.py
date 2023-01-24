from django.db import models
from django.contrib.auth.models import User


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário', unique=False, blank=True, null=True)
    date = models.DateField()
    category = models.CharField(max_length=500)
    title = models.CharField(max_length=500, blank=True, null=True)
    value = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
