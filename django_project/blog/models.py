from django.db import models

# Create your models here.


class ModelMixin(object):
    """docstring for ModelMin"""

    def __str__(self):
        try:
            return self.name
        except Exception:
            return self.title


class Author(ModelMixin, models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)


class Category(ModelMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author)


class Tag(ModelMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author)


class Post(ModelMixin, models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
