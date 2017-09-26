# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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


#w文章模型
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    desc = models.CharField(max_length=50,verbose_name="w文章描述")
    content = models.TextField(verbose_name="文章内容")
    click_count = models.IntegerField(default=0,verbose_name="点击次数")
    is_recommend = models.BooleanField(default=False,verbose_name="是否推荐")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")#
#    user = models.ForeignKey(User,verbose_name="用户")
    category = models.ForeignKey(Category,blank=True,null=True,verbose_name="分类")
    tag = models.ManyToManyField(Tag,verbose_name="标签")

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

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
