# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
import logging
from models import Article,Category,Tag,Links
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger

# Create your views here.
logger = logging.getLogger(__name__)

def global_settings(request):
    SITE_URL = settings.SITE_URL
    SITE_NAME = settings.SITE_NAME
    SITE_TITLE = settings.SITE_TITLE
    SITE_DESC = settings.SITE_DESC
    archive_list = Article.objects.data_article()
    category_list = Category.objects.all()[:6]
    tag_list = Tag.objects.all()
    links_list = Links.objects.all()
    #logger.error("global setting ")
    return locals()

#首页
def index(request):
    #分类信息获取
    try:
        article_list = Article.objects.all()
        article_list = getpage(request,article_list)
    except Exception as e:
        logger.error(e)

    #文章归档

    #广告数据

    #最新文章数据
    return render(request,'app/index.html',locals())

#归档页面
def archive(request):
    try:
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.filter(date_publish__icontains = year + '-' + month)
        article_list = getpage(request,article_list)
    except Exception as e:
        logger.error(e)
    return render(request,'app/archive.html',locals())

def getpage(request,article_list):
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

def article(request):
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'app/article.html', locals())

def category(request):
    try:
        # 获取分类类型id
        cid = request.GET.get('cid', None)
        try:
            #获取分类信息
            category = Category.objects.filter(pk=cid).values()[0]
            print category
        except Category.DoesNotExist:
            return render(request, 'failure.html', {'reason': '该分类不存在'})
        #获取分类文章
        article_list = Article.objects.filter(category_id = cid)
        article_list = getpage(request,article_list)
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'app/category.html', locals())

def tag(request):
    try:
        # 获取分类类型id
        tid = request.GET.get('tid', None)
        print tid
        try:
            #获取分类信息
            tag = Tag.objects.filter(pk=tid).values()[0]
        except Tag.DoesNotExist:
            return render(request, 'failure.html', {'reason': '该标签文章不存在'})
        #获取分类文章
        article_list = Article.objects.filter(tag = tid)
        print article_list
        article_list = getpage(request,article_list)
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'app/tag.html', locals())