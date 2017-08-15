from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import PostForm
from blog import models

# Create your views here.


def post_add(request):
    if request.method == "POST":
        f = PostForm(request.POST)

        if f.is_valid():
            f.save()
            return redirect('post_add')
    else:
        f = PostForm()

    return render(request, 'cadmin/post_add.html', {'form': f})


def post_update(request, pid):
    post = get_object_or_404(models.Post, id=pid)

    if request.method == 'POST':
        f = PostForm(request.POST, instance=post)
        if f.is_valid():
            f.save()

            return redirect('post_update', post.id)
    else:
        f = PostForm(instance=post)

    return render(request, 'cadmin/post_update.html',
        {'form': f, 'post': post})
