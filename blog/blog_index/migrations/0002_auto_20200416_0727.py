# Generated by Django 3.0.5 on 2020-04-16 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 7, 27, 56, 188565), verbose_name='DatePublished'),
        ),
    ]
