# Generated by Django 5.0.1 on 2024-01-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='CricVision', max_length=255),
        ),
    ]
