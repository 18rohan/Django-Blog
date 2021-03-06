# Generated by Django 3.0.5 on 2020-04-16 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_published', models.DateTimeField(default=datetime.datetime(2020, 4, 16, 7, 7, 16, 361105), verbose_name='DatePublished')),
                ('blog_author', models.CharField(max_length=200)),
            ],
        ),
    ]
