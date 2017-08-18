#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-18 10:21:29
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustromUserCreateFrom(forms.Form):
    # TODO: Define form fields here
    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(
        label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count() > 0:
            raise ValidationError('Username %s already use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count() > 0:
            raise ValidationError('Email %s alread use.' % email)

        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password not match.")

        return password2

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password2'])

        return user
