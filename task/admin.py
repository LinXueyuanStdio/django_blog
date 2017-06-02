# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed','create_date')
    search_fields = ('title', 'description', 'completed','create_date')
    list_filter = ("create_date",)
    date_hierarchy = 'create_date'

admin.site.register(Task, TaskAdmin)