from django.contrib import admin
 
from .models import Column, Article, Tag
 
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'intro')
 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'author')
    search_fields = ('title', 'author', 'column', 'tag', 'content', 'date_time')
    list_filter = ("date_time",)
    # raw_id_fields = ('tag', )    
    date_hierarchy = 'date_time'
 
admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)