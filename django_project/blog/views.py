from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Author, Tag, Category, Post

# Create your views here.


def index(request):
    return HttpResponse("Hello Django")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, pid):
    post = Post.objects.get(id=pid)
    return render(request, 'blog/post_detail.html', {"post": post})


def posts_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'blog/post_by_category.html', context)


def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, 'blog/post_by_tag.html', context)
