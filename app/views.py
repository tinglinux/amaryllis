# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
import logging
from models import Article
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger

# Create your views here.
logger = logging.getLogger(__name__)

def global_settings(request):
    #logger.error("global setting ")
    return {"SITE_NAME":settings.SITE_NAME,"SITE_TITLE":settings.SITE_TITLE,"SITE_DESC":settings.SITE_DESC}

def index(request):
    #分类信息获取
    try:
        article_list = Article.objects.all()
        paginator = Paginator(article_list,10)
        page = request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
        archive_list = Article.objects.data_article()
    except Exception as e:
        logger.error(e)

    #文章归档

    #广告数据

    #最新文章数据
    return render(request,'app/index.html',locals())

def archive(request):
    try:
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.filter(date_publish__icontains = year + '-' + month)
        paginator = Paginator(article_list,10)
        page = request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
        archive_list = Article.objects.data_article()
    except Exception as e:
        logger.error(e)
    return render(request,'app/archive.html',locals())
