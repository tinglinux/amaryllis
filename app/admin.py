# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tag,Article,Category,Links
# Register your models here.


#自定义文章管理样式
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','desc','content','tag','category']
    list_display = ['title','desc','date_publish']

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
        )

admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Links)