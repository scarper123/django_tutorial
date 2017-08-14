#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-14 16:07:20
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django import forms


class AuthorForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    active = forms.BooleanField(required=False)
    created_on = forms.DateTimeField()
    last_logged_in = forms.DateTimeField()
