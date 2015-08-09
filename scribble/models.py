from django.db import models
from tinymce.models import HTMLField
from scribbler.settings import MEDIA_ROOT


class Writeup(models.Model):
    title = models.CharField(max_length=512)
    content = HTMLField()
    posted_on = models.DateField(auto_now_add=True)
    pic = models.ImageField(upload_to=MEDIA_ROOT)
    tiny_pic = models.ImageField(upload_to=MEDIA_ROOT)


class Piece(models.Model):
    title = models.CharField(max_length=512)
    brief = models.CharField(max_length=256)
    posted_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content_id = models.CharField(max_length=256)
    tiny_pic = models.ImageField(upload_to=MEDIA_ROOT)


class Comment(models.Model):
    comment = models.CharField(max_length=8192)
    commentator = models.CharField(max_length=256)
    post_id = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


class Like(models.Model):
    owner = models.CharField(max_length=256)
    subject = models.CharField(max_length=100)

