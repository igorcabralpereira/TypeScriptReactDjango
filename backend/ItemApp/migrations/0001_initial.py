# Generated by Django 4.1.3 on 2022-11-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=500)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
            ],
        ),
    ]
