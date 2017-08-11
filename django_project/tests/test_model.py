#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-11 09:31:31
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from blog.models import Author


def add_authors():
    Author.objects.bulk_create([
        Author(name="tom", email="tom@email.com"),
        Author(name="jerry", email="jerry@email.com"),
        Author(name="spike", email="spike@email.com"),
        Author(name="tyke", email="tyke@email.com")
    ])


if __name__ == '__main__':
    add_authors()
