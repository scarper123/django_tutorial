from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from blog.models import Author, Tag, Category, Post
from blog import forms
# Create your views here.


def index(request):
    return HttpResponse("Hello Django")


def post_list(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, id=pid)
    return render(request, 'blog/post_detail.html', {"post": post})


def posts_by_category(request, category_slug):
    # category = Category.objects.get(slug=category_slug)
    # posts = Post.objects.filter(category__slug=category_slug)
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'blog/post_by_category.html', context)


def posts_by_tag(request, tag_slug):
    # tag = Tag.objects.get(slug=tag_slug)
    # posts = Post.objects.filter(tags__name=tag)
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, 'blog/post_by_tag.html', context)


def posts_by_author(request, author_name):
    # author = Author.objects.get(name=author_name)
    # posts = Post.objects.filter(author__name=author_name)
    author = get_object_or_404(Author, name=author_name)
    posts = get_list_or_404(Post.objects.order_by("-id"), author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/post_by_author.html', context)


def feedback(request):
    if request.method == "POST":
        f = forms.FeedbackForm(request.POST)
        if f.is_valid():
            f.save()

            return redirect('feedback')

    else:
        f = forms.FeedbackForm()

    return render(request, 'blog/feedback.html', {'form': f})
