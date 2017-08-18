#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-18 15:33:42
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.contrib.sitemaps import Sitemap
from blog import models


class PostSitMap(Sitemap):
    """docstring for PostSitMap"""

    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return models.Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
