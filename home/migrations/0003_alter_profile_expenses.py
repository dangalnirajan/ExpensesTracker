# Generated by Django 3.2.12 on 2023-10-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20231010_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(default=0),
        ),
    ]
