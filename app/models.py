# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import Counter
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#标签模型
class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name="标签名称")

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.name


#分类模型
class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="分类名称")
    index = models.IntegerField(default=999,verbose_name="分类排序")

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __str__(self):
        return self.name

#文章model管理器
#进行文章按月归档，并统计每月文章数量
class ArticleManager(models.Manager):
    def data_article(self):
        article_date_publish = []
        article_archive_list = {}
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y%m')
            article_date_publish.append(date)

        article_archive_list = dict(Counter(article_date_publish))
        return article_archive_list

#w文章模型
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    desc = models.CharField(max_length=50,verbose_name="文章描述")
    content = models.TextField(verbose_name="文章内容")
    click_count = models.IntegerField(default=0,verbose_name="点击次数")
    is_recommend = models.BooleanField(default=False,verbose_name="是否推荐")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")#
#    user = models.ForeignKey(User,verbose_name="用户")
    category = models.ForeignKey(Category,blank=True,null=True,verbose_name="分类")
    tag = models.ManyToManyField(Tag,verbose_name="标签")

    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def add_click(self):
        self.click_count +=1
        self.save(update_fields=['click_count'])

    def __str__(self):
        return self.title

#友情链接
class Links(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题")
    desc = models.CharField(max_length=200,verbose_name="友情链接描述")
    callback_url = models.URLField(verbose_name="url地址")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    index = models.IntegerField(default=999,verbose_name="排序")

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __str__(self):
        return self.title

#广告
class Ad(models.Model):
    title = models.CharField(max_length=50,verbose_name="广告标题")
    desc = models.CharField(max_length=200,verbose_name="广告描述")
    image_url = models.ImageField(upload_to="ad/%Y/%m",verbose_name="图片路径")
    callback_url = models.URLField(null=True,blank=True,verbose_name="回调URL")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    index = models.IntegerField(default=999,verbose_name="排序")

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title

'''
#用户模型
class User(models.Model):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username


#评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)
'''
