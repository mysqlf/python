#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
from django.conf.urls import url
from django.contrib import admin
from blog.views import blog_index

from blog.views import *
urlpatterns=[
    #这个name在页面模板使用url 方法时会用到
    url(r'^index/$', ArticleListView.as_view(),name='blog_index'),
    url(r'^$', ArticleListView.as_view()),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    url(r'^article/(?P<title>\w+\.?\w+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<title>\w+\.?\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),
]

