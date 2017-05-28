# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
 
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'email','url')
    search_fields = ('name', 'text', 'email', 'url', 'created_time')
    list_filter = ("created_time",)
    # raw_id_fields = ('tag', )    
    date_hierarchy = 'created_time'

admin.site.register(Comment, CommentAdmin)

