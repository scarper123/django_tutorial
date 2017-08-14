#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 15:00:13
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pid>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<category_slug>[\w-]+)/$',
        views.posts_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$',
        views.posts_by_tag, name='post_by_tag'),
    url(r'^author/(?P<author_name>[\w-]+)/$',
        views.posts_by_author, name='post_by_author'),
]
