#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 15:00:13
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.conf.urls import url
from cadmin import views

urlpatterns = [
    url(r'^post/add/$', views.post_add, name='post_add'),
    url(r'^post/update/(?P<pid>\d+)$', views.post_update, name='post_update'),
]
