# -*- coding: utf-8 -*-
from django import template
register = template.Library()

# 定义一个将日期中的月份转换为大写的过滤器，如8转换为八
@register.filter
def month_to_upper(key):
        return ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一', '十二'][key.month-1]