from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class ModelMixin(object):
    """docstring for ModelMin"""

    def __str__(self):
        try:
            return self.name
        except Exception:
            return self.title

    def get_absolute_url(self):
        raise NotImplementedError


class Author(ModelMixin, models.Model):
    """docstring for Author"""
    # name = models.CharField(max_length=100, unique=True)
    # email = models.EmailField(unique=True)
    # active = models.BooleanField(default=False)
    # created_on = models.DateTimeField(auto_now_add=True)
    # last_logged_in = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, null=True, blank=True)

    # additional fields
    phone = models.IntegerField(blank=True, default=1)
    activation_key = models.CharField(default=1, max_length=255)
    email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('post_by_author', args=[self.user.username])


class Category(ModelMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])


class Tag(ModelMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author)

    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])


class Post(ModelMixin, models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    # content = models.TextField()
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Feedback(ModelMixin, models.Model):

    name = models.CharField(max_length=200, help_text='Name of the sender')
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return self.name + '-' + self.email

    def get_absolute_url(self):
        return reverse('feedback')
