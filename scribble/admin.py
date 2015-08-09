from django.contrib import admin

# Register your models here.

from django.contrib import admin
from scribble.models import Writeup, Comment, Piece


class WriteupAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_on')

    def save_model(self, request, obj, form, change):
        obj.title = obj.title.replace(' ', '_')
        obj.save()
        Piece(title=obj.title, brief=obj.content[:100], content_id=obj.id, tiny_pic=obj.tiny_pic).save()


admin.site.register(Writeup, WriteupAdmin)


