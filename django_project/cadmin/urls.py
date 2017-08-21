#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 15:00:13
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from cadmin import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/add/$', views.post_add, name='post_add'),
    url(r'^post/delete/(?P<pid>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^post/update/(?P<pid>\d+)/$', views.post_update, name='post_update'),
    url(r'^category/$', views.category_list, name='category_list'),
    url(r'^category/add/$', views.category_add, name='category_add'),
    url(r'^category/update/(?P<cid>\d+)/$', views.category_update, name='category_update'),
    url(r'^category/delete/(?P<cid>\d+)/$', views.category_delete, name='category_delete'),

    url(r'^tag/$', views.tag_list, name='tag_list'),
    url(r'^tag/add/$', views.tag_add, name='tag_add'),
    url(r'^tag/update/(?P<cid>\d+)/$', views.tag_update, name='tag_update'),
    url(r'^tag/delete/(?P<cid>\d+)/$', views.tag_delete, name='tag_delete'),

    url(r'^accounts/login/$', views.login,
        kwargs={'template_name': 'cadmin/login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', auth_views.logout,
        kwargs={'template_name': 'cadmin/logout.html'}, name='auth_logout'),
    url(r'^password-change-done/$', auth_views.password_change_done,
        name='password_change_done'),
    url(r'^password-change/$', auth_views.password_change,
        kwargs={'post_change_redirect': 'password_change_done'},
        name='password_change'),
    url(r'^register/$', views.register, name='register'),
    url(r'^activate-account/$', views.activate_account, name='activate_account'),
]
