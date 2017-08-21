from django.conf import settings
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404, get_list_or_404

from blog import models
from blog.forms import PostForm, CategoryForm, TagForm
from cadmin import forms
from django_project import helpers


# Create your views here.

@login_required
def post_add(request):
    print('is superuser -> %s' % request.user.is_superuser)
    if request.method == "POST":
        f = PostForm(request.POST)

        if f.is_valid():
            if request.POST.get('author') == "" and request.user.is_superuser:
                new_post = f.save(commit=False)
                author = models.Author.objects.get(user__username='staff')
                new_post.author = author
                new_post.save()
                f.save_m2m()
            elif request.POST.get('author') and request.user.is_superuser:
                new_post = f.save()
            else:
                new_post = f.save(commit=False)
                print("new_post.tags")
                new_post.author = models.Author.objects.get(user__username=request.user.username)
                new_post.save()
                f.save_m2m()

            # f.save()
            return redirect('post_add')
    else:
        f = PostForm()

    return render(request, 'cadmin/post_add.html', {'form': f})


@login_required
def post_list(request):
    if request.user.is_superuser:
        post_list = models.Post.objects.order_by("-id").all()
    else:
        post_list = models.Post.objects.filter(author__user__username=request.user.username).order_by("-id")

    posts = helpers.pg_records(request, post_list)
    return render(request, 'cadmin/post_list.html', {'posts': posts})


@login_required
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


def login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    return auth_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def home(request):
    return render(request, 'blog/admin_page.html')


def register(request):
    if request.method == 'POST':
        f = forms.CustromUserCreateFrom(request.POST)
        if f.is_valid():
            # send email verification now
            activation_key = helpers.generate_activation_key(
                username=request.POST['username'])

            subject = "The Great Django Blog Account Verification"

            message = """
Please visit the following link to verify you account {}://{}/cadmin/activate-account/?key={}
            """.format(request.scheme, request.get_host(), activation_key)

            error = False
            try:
                send_mail(subject, message, settings.SERVER_EMAIL,
                          [request.POST['email']])
            except Exception as e:
                print(e)
                messages.add_message(
                    request, messages.INFO, 'Unable to send email verification. Please try again.')
                error = True
            else:
                messages.add_message(
                    request, messages.INFO,
                    'Account created! Click on the link send to your email to activate the account.')

            if not error:
                u = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    request.POST['password2'],
                    is_active=0)

                author = models.Author()
                author.activation_key = activation_key
                author.user = u
                author.save()

                return redirect('register')

    else:
        f = forms.CustromUserCreateFrom()

    return render(request, 'cadmin/register.html', {'form': f})


def activate_account(request):
    key = request.GET['key']
    if not key:
        raise Http404()

    r = get_object_or_404(
        models.Author, activation_key=key, email_validated=False)

    r.user.is_active = True
    r.user.save()
    r.email_validated = True
    r.save()

    return render(request, 'cadmin/activated.html')


@login_required
def post_delete(request, pid):
    post = get_object_or_404(models.Post, id=pid)
    post = post.delete()
    messages.add_message(request, messages.INFO, "Delete post successful %s" % str(post))
    return redirect('post_list')


@login_required
def category_list(request):
    if request.user.is_superuser:
        categories = models.Category.objects.order_by("-id").all()
    else:
        categories = models.Category.objects.filter(author__user__username=request.user.username).order_by("-id")

    categories = helpers.pg_records(request, categories, 5)

    return render(request, 'cadmin/category_list.html', {'categories': categories})


@login_required
def category_add(request):
    if request.method == "POST":
        f = CategoryForm(request.POST)

        if f.is_valid():
            if request.POST.get('author') == "" and request.user.is_superuser:
                author = get_object_or_404(models.Author, user__username="staff")
                new_category = f.save(False)
                new_category.author = author
                new_category.save()
                f.save_m2m()
            elif request.POST.get('author') and request.user.is_superuser():
                f.save()
            else:
                new_category = f.save(False)
                new_category.author = get_object_or_404(models.Author, user=request.user)
                new_category.save()
                f.save_m2m()
            return redirect('category_list')

    else:
        f = CategoryForm()
    return render(request, 'cadmin/category_add.html', {"form": f})


@login_required
def category_update(request, cid):
    category = get_object_or_404(models.Category, id=cid)
    if request.method == "POST":
        f = CategoryForm(request.POST, instance=category)
        if f.is_valid():
            f.save()

            return redirect('category_list')
    else:
        f = CategoryForm(instance=category)

    return render(request, 'cadmin/category_update.html', {"form": f})


@login_required
def category_delete(request, cid):
    category = get_object_or_404(models.Category, id=cid)
    category.delete()
    messages.add_message(request, messages.INFO, "Delete category %s succeed." % category.name)
    return redirect('category_list')


@login_required
def tag_list(request):
    if request.user.is_superuser:
        tag_list = get_list_or_404(models.Tag)
    else:
        tag_list = get_list_or_404(models.Tag, author__user__username=request.user.username)
    tags = helpers.pg_records(request, tag_list)
    return render(request, 'cadmin/tag_list.html', {'tags': tags})


@login_required
def tag_add(request):
    if request.method == "POST":
        f = TagForm(request.POST)
    else:
        f = TagForm()
    return render(request, 'cadmin/tag_add.html', {"form": f})


@login_required
def tag_update(request, tid):
    return None


@login_required
def tag_delete(request, tid):
    return None
