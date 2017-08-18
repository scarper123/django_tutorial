#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 15:00:13
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.conf.urls import url
from cadmin import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/add/$', views.post_add, name='post_add'),
    url(r'^post/update/(?P<pid>\d+)$', views.post_update, name='post_update'),
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
