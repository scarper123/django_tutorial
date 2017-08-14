from django.test import TestCase
import unittest
# Create your tests here.

from blog.forms import AuthorForm


class AuthorFormTest(TestCase):
    """docstring for AuthorFormTest"""

    def __init__(self, *args, **kwargs):
        super(AuthorFormTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def test_form_bound(self):
        f = AuthorForm()
        self.assertTrue(f.is_bound)


if __name__ == '__main__':
    unittest.main()
