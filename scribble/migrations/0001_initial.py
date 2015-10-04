# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=8192)),
                ('commentator', models.CharField(max_length=256)),
                ('post_id', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('brief', models.CharField(max_length=256)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content_id', models.CharField(max_length=256)),
                ('tiny_pic', models.ImageField(upload_to=b'E:\\Djangoproj\\scribble\\scribbler\\media\\')),
            ],
        ),
        migrations.CreateModel(
            name='Writeup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('content', tinymce.models.HTMLField()),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('pic', models.ImageField(upload_to=b'E:\\Djangoproj\\scribble\\scribbler\\media\\')),
                ('tiny_pic', models.ImageField(upload_to=b'E:\\Djangoproj\\scribble\\scribbler\\media\\')),
            ],
        ),
    ]
