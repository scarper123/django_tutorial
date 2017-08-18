from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from blog.forms import PostForm
from blog import models
from cadmin import forms
from django_project import helpers


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


def login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    return auth_views.login(request, **kwargs)


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
                    request, messages.INFO, 'Account created! Click on the link send to your email to activate the account.')

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
