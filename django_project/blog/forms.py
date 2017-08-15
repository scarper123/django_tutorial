#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-14 16:07:20
# @Author  : Shanming Liu (shanming.liu@ericsson.com)
# @Link    : ${link}
# @Version : $Id$

from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from blog import models


# class AuthorForm(forms.Form):
#     # TODO: Define form fields here
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     active = forms.BooleanField(required=False)
#     created_on = forms.DateTimeField()
#     last_logged_in = forms.DateTimeField()

#     def save(self):
#         new_author = models.Author.objects.create(
#             name=self.cleaned_data['name'],
#             email=self.cleaned_data['email'],
#             active=self.cleaned_data['active'],
#             created_on=self.cleaned_data['created_on'],
#             last_logged_in=self.cleaned_data['last_logged_in'])
#         return new_author

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         name_l = name.lower()
#         if name_l == 'admin' or name_l == 'author':
#             raise ValidationError("Author name can't be 'admin/author")
#         return name

#     def clean_email(self):
#         return self.cleaned_data['email'].lower()


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l == 'admin' or name_l == 'author':
            raise ValidationError("Author name can't be 'admin/author")
        return name

    def clean_email(self):
        return self.cleaned_data['email'].lower()


class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l in ['tag', 'add', 'update']:
            raise ValidationError("Tag name can't be {}".format(name))
        return name

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = '__all__'

    def clean_name(self):
        n = self.cleaned_data['name']
        if n.lower() == "tag" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Category name can't be '{}'".format(n))
        return n

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ('title', 'content', 'author', 'category', 'tags',)

    def clean_name(self):
        n = self.cleaned_data['title']
        if n.lower() == "post" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Post name can't be '{}'".format(n))
        return n

    def clean(self):
        # call the parent clean method
        cleaned_data = super(PostForm, self).clean()
        title = cleaned_data.get('title')
        # if title exists create slug from title
        if title:
            self.slug = slugify(title)

        return cleaned_data


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = '__all__'
