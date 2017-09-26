# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
import logging


# Create your views here.
logger = logging.getLogger(__name__)

def global_settings(request):
    #logger.error("global setting ")
    return {"SITE_NAME":settings.SITE_NAME,"SITE_TITLE":settings.SITE_TITLE,"SITE_DESC":settings.SITE_DESC}

def index(request):
    logger.error("请求失败")
    return render(request,'app/index.html')