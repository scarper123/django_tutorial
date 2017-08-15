import unittest
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
import pprint


import django
django.setup()
from django.test import TestCase, Client

from blog.forms import AuthorForm
from blog import models

# Create your tests here.


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


if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(AuthorFormTest("test_form_print"))
    runner.run(suite)
