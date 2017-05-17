#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import F
from django.views.generic.list import ListView
from django.shortcuts import render_to_response
# Create your views here.

from blog.models import Article


from django.views.generic.edit import FormView
from blog.forms import ArticlePublishForm

from django.http import Http404
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

class ArticleEditView(FormView):
    template_name="blog/article_publish.html"
    form_class=ArticlePublishForm
    article=None

    def get_initial(self,**kwargs):
        title=self.kwargs.get('title')
        try:
            self.article=Article.objects.get(title=title)
            initial={
                'title':title,
                'content':self.article.content_md,
                'tags':self.article.tags,
            }
            return initial
        except Article.DoesNotExist:
            raise Http404('Article does not exist')

    def form_valid(self,form):
        form.save(self.request,self.article)
        return super(ArticleEditView,self).form_valid(form)

    def get_success_url(self):
        title=self.request.POST.get('title')
        success_url=reverse('article_detail',args=(title,))
        return success_url

class ArticleDetailView(DetailView):
    template_name='blog/article_detail.html'
    def get_object(self,**kwargs):
        title=self.kwargs.get('title')
        try:
            article=Article.objects.get(title=title)
            article.views+=1
            article.save()
            article.tags=article.tags.split()
        except Article.DoesNotExist:
            raise Http404('Article does not exist')
        return article


class ArticlePublishView(FormView):
    template_name="blog/article_publish.html"
    form_class=ArticlePublishForm
    success_url='/blog/'
    def form_valid(self,form):
        form.save(self.request.user.username)
        return super(ArticlePublishView,self).form_valid(form)

class ArticleListView(ListView):
    template_name='blog/blog_index.html'
    def get_queryset(self,**kwargs):
        object_list=Article.objects.all().order_by(F('created').desc())[:100]
        paginator=Paginator(object_list, 10)   
        page=self.request.GET.get('page')
        try:
            object_list=paginator.page(page)
        except PageNotAnInteger:
            object_list=paginator.page(1)
        except EmptyPage:
            object_list=paginator.page(paginator.num_pages)
        return object_list

        

def blog_index(request):
	return render_to_response('blog/blog_index.html')
