import unittest
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
import pprint


import django
django.setup()
from django.test import TestCase, Client
from django.core.paginator import Paginator, EmptyPage
from django.contrib.sessions.models import Session

from blog.forms import AuthorForm
from blog import models

# Create your tests here.


class Mixin(object):
    """docstring for Mixin"""

    def __init__(self, arg):
        super(Mixin, self).__init__()
        self.arg = arg


class AuthorFormTest(TestCase):
    """docstring for AuthorFormTest"""

    def __init__(self, case_name=None, *args, **kwargs):
        super(AuthorFormTest, self).__init__(case_name)

    def setUp(self):
        self.client = Client()

    # def test_request(self):
    #     res = self.client.get('blog')
    #     print(res)

    def test_form_bound(self):
        f = AuthorForm()
        self.assertFalse(f.is_bound)
        f = AuthorForm({})
        self.assertTrue(f.is_bound)
        f = AuthorForm({})
        with self.assertRaises(AttributeError):
            f.cleaned_data

        print(f.is_valid())
        pprint.pprint(f.fields)
        pprint.pprint(f.errors.as_json())
        pprint.pprint(f.cleaned_data)

    def test_form_print(self):
        f1 = AuthorForm()
        print(f1.as_table())
        f2 = AuthorForm({'name': 'author', 'active': True})
        print(f2.as_table())


class ModelTest(TestCase):
    """docstring for ModelTest"""

    def __init__(self, case_name=None, *args, **kwargs):
        super(ModelTest, self).__init__(case_name)

    def test_post_filter(self):
        posts = models.Post.objects.filter()
        print(posts)


class PaginatorTest(TestCase):
    """docstring for PaginatorTest"""

    def __init__(self, case_name=None, *args, **kwargs):
        super(PaginatorTest, self).__init__(case_name)

    def test_paginator(self):
        paginator = Paginator(models.Post.objects.all(), 5)
        print(getattr(models.Post.objects.all(), 'ordered', None))
        print(paginator.count)
        print(paginator.num_pages)

        page1 = paginator.page(1)
        print(page1.object_list)
        with self.assertRaises(EmptyPage):
            page2 = paginator.page(paginator.num_pages + 1)


class SessionTest(TestCase):
    """docstring for SessionTest"""

    def __init__(self, case_name=None, *args, **kwargs):
        super(SessionTest, self).__init__(case_name)

        self.client = Client()

    def test_save_session(self):
        response = self.client.get(
            'http://127.0.0.1:8000/blog/save-session-data/')
        print(response.content)
        print(response.cookies)

        self.test_query_session()

    def test_query_session(self):
        sessions = Session.objects.all()
        for session in sessions:
            pprint.pprint(session)


if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(SessionTest("test_query_session"))
    runner.run(suite)
