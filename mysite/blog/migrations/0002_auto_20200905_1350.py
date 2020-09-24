# Generated by Django 2.2.2 on 2020-09-05 13:50

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to=blog.models.upload_location),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
