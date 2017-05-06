# -*- coding: utf-8 -*-  
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed
from blog.models import Article, Tag, History, Source, SourceClass
from datetime import datetime

site = {
    'title' : u"XiChen",
    'subtitle' : 'He who thinks wins',
    
    'description' : '嗨，我是兮尘，全栈数据学徒。这里没有花俏艳丽的魔法，没有苍蛮霸道的斗气，有的，仅仅是繁衍到巅峰的代码！',
    'welcome_message' : '欢迎来到我的数据世界！',
    'blog_button':{'title':u"博客", 'description':"blog-button-description"},
    'nav' : [
        {'title':u'GitHub', 'url':'https://github.com/LinXueyuanStdio', 'description':"description", 'in_site':False},
        {'title':u'目录', 'url':'archives', 'description':"description", 'in_site':True},
        {'title':u'资源', 'url':'source', 'description':"description", 'in_site':True},
        {'title':u'RSS', 'url':'RSS', 'description':"description", 'in_site':True},
        {'title':u'关于', 'url':'about_me', 'description':"description", 'in_site':True}
    ],
    'social' : {
        'weibo':'dd',
        'github':'LinXueyuanStdio',
        'twitter':'LinXueyuanStdio',
        'zhihu':'zhihu',
        'mail':'mail',
        'copyright':'copyright'
    },
    'cover_color' : 'slate'
}

def base(request):
    page = {'layout':'no'}
    return render(request, 'base.html', {'site':site, 'page':page})

def home(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 10) #每页显示两个
    pages = request.GET.get('page')
    page = {'layout':'post'}
    try :
        post_list = paginator.page(pages)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list,'site':site, 'page':page})

def archives(request) :
    page = {'layout':'post'}
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html',
                 {'post_list' : post_list,
                  'error' : False,
                  'site':site, 
                  'page':page})

def detail(request, id):
    page = {'layout':'post'}
    try:
        post = Article.objects.get(id=str(id))
        tags = post.tag.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post, 'tags': tags, 'site':site, 'page':page})

def about_me(request) :
    page = {'layout':'post'}
    try:
        post_list = History.objects.all()
    except History.DoesNotExist :
        raise Http404
    return render(request, 'aboutme.html', {'post_list': post_list, 'site':site, 'page':page})

def source(request) :
    page = {'layout':'post'}
    try:
        post_class_list = SourceClass.objects.all()
        post_list = Source.objects.all()
    except Source.DoesNotExist :
        raise Http404
    return render(request, 'source.html', {'post_class_list':post_class_list,
        'post_list': post_list, 'site':site, 'page':page})


def search_tag(request, tag) :
    page = {'layout':'post'}

    try:
        tag_id = tag[0]
        post_list = Article.objects.filter(tag = tag_id) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list, 'site':site, 'page':page})

def blog_search(request):
    page = {'layout':'post'}
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', 
                    {'post_list' : post_list,
                     'error' : True, 
                     'site':site, 
                     'page':page})
            else :
                return render(request,'archives.html',
                    {'post_list' : post_list,
                     'error' : False, 
                     'site':site, 
                     'page':page})
    return redirect('/')

class RSSFeed(Feed) :
    page = {'layout':'post'}
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content

