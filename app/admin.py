# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tag,Article,Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','desc','content']
    list_display = ['title','desc','date_publish']

admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)