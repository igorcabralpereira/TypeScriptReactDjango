# Generated by Django 4.1.3 on 2022-11-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
