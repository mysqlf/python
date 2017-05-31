#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import F
from django.views.generic.list import ListView
from django.shortcuts import render_to_response

from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

from blog.models import Article


from django.views.generic.edit import FormView
from blog.forms import ArticlePublishForm

from django.http import Http404
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
import qrcode
import os
import datetime
#登陆控制
class AdminRequiredMixin(object):
    @classmethod
    def as_view(cls,**initkwargs):
        view=super(AdminRequiredMixin,cls).as_view(**initkwargs)
        return staff_member_required(view)

#文章编辑(继承权限控制,以及表单视图)
class ArticleEditView(AdminRequiredMixin,FormView):
    template_name="blog/article_publish.html"
    form_class=ArticlePublishForm
    article=None
#内部方法
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
#文章详情
class ArticleDetailView(DetailView):
    template_name='blog/article_detail.html'
    # def erweima(self,request):
        
        
    #     path=BASE_DIR+'upload/img/'+url+'.png'
    #     if not os.path.isfile(path):
    #         qr = qrcode.QRCode(
    #             version=1,
    #             error_correction=qrcode.constants.ERROR_CORRECT_L,
    #             box_size=10,
    #             border=4,
    #         )
    #         qr.add_data(url)
    #         qr.make(fit=True)
    #         img = qr.make_image()
    #         img.save(path)
    #     return path

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

#发表文章
class ArticlePublishView(AdminRequiredMixin,FormView):
    template_name="blog/article_publish.html"
    form_class=ArticlePublishForm
    success_url='/blog/'
    def form_valid(self,form):
        form.save(self.request.user.username)
        return super(ArticlePublishView,self).form_valid(form)
#文章列表
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
