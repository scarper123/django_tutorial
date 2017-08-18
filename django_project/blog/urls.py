#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 15:00:13
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.conf.urls import url
from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps.views import sitemap
from blog import views
from blog.sitemaps import PostSitMap


sitemaps = {
    'posts': PostSitMap
}

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pid>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<category_slug>[\w-]+)/$',
        views.posts_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$',
        views.posts_by_tag, name='post_by_tag'),
    url(r'^author/(?P<author_name>[\w-]+)/$',
        views.posts_by_author, name='post_by_author'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^cookie/$', views.test_cookie, name='test_cookie'),
    url(r'^test-session/$', views.test_session, name='test_cookie'),
    url(r'^test-delete/$', views.test_delete, name='test_cookie'),

    url(r'^save-session-data/$',
        views.save_session_data, name='save_session_data'),
    url(r'^access-session-data/$', views.access_session_data,
        name='access_session_data'),
    url(r'^delete-session-data/$', views.delete_session_data,
        name='delete_session_data'),
    url(r'^lousy-login/$', views.lousy_login, name='lousy_login'),
    url(r'^lousy-secret/$', views.lousy_secret, name='lousy_secret'),
    url(r'^lousy-logout/$', views.lousy_logout, name='lousy_logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    url(r'^about/$', flat_views.flatpage, {'url': '/about/'}, name='about'),
    url(r'^eula/$', flat_views.flatpage, {'url': '/eula/'}, name='eula'),
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
