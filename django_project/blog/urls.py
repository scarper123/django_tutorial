#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 15:00:13
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^today/$', views.today_is, name='blog_today'),
]
