# -*- coding: utf-8 -*-  
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    url = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['-name']  # 按照哪个栏目排序

class Tag(models.Model):
    tag_name = models.CharField('标签', max_length=256)

    def __str__(self):
        return str(self.id) + str(self.tag_name)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        ordering = ['-tag_name']  # 按照哪个栏目排序

class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
    tag = models.ManyToManyField(Tag, verbose_name='标签')  # 博客标签 可为空
    
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期

    title = models.CharField('标题', max_length=256)#博客题目
    content = models.TextField('内容', default='', blank=True) #博客文章正文
    
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:80%s" % path

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-date_time']

class History(models.Model):
    # update time
    date_time = models.DateTimeField(auto_now_add = True)
    # text
    things = models.CharField('标题', max_length=256)
    raw_url = models.CharField('引用地址', max_length=256)

    def __str__(self):
        return self.things

    class Meta:
        verbose_name = '历史记录'
        verbose_name_plural = '历史记录'
        ordering = ['-date_time']

class SourceClass(models.Model):
    src_class = models.CharField('类别', max_length=128)
    intro = models.CharField('简介', max_length=128)

    def __str__(self):
        return self.src_class

    class Meta:
        verbose_name = '资源种类'
        verbose_name_plural = '资源种类'

class Source(models.Model):
    src_class = models.ForeignKey('SourceClass',blank=True, null=True, verbose_name='归属类别')
    src_title = models.CharField('标题', max_length=128)
    src_marks = models.CharField('标记',blank=True, null=True, max_length=128)
    src_url = models.CharField('引用地址', max_length=256)
    src_hint = models.CharField('显示地址', max_length=256)

    def __str__(self):
        return self.src_title

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = '资源'
        ordering = ['-src_class','-src_marks']