# Generated by Django 4.1.3 on 2022-11-26 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ItemApp', '0005_rename_user_id_items_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='user',
            new_name='usuario',
        ),
    ]