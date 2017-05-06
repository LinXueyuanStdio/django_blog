from django.contrib import admin
 
from .models import Column, Article, Tag, History, Source, SourceClass
 
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

class HistoryAdmin(admin.ModelAdmin):
	list_display = ('date_time', 'things', 'raw_url')

class SourceAdmin(admin.ModelAdmin):
	list_display = ( 'src_title', 'src_marks','src_class', 'src_url')
	list_filter = ('src_hint',)

class SourceClassAdmin(admin.ModelAdmin):
	list_display = ('src_class', 'intro')

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(SourceClass, SourceClassAdmin)