# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u63cf\u8ff0'),
        ),
    ]
