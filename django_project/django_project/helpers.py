#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-16 13:43:34
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def pg_records(request, all_list, num=10):
    page = request.GET.get('page', 1)
    paginator = Paginator(all_list, num)

    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    return records
