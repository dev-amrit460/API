# Generated by Django 4.0.5 on 2022-06-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
