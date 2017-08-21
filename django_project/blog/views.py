from django.contrib import auth
from django.contrib import messages
from django.core.mail import mail_admins
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from blog import forms
from blog.models import Author, Tag, Category, Post
from django_project import helpers


# Create your views here.


def index(request):
    return HttpResponse("Hello Django")


def post_list(request):
    post_list = Post.objects.order_by("-id").all()
    posts = helpers.pg_records(request, post_list)
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, id=pid)
    return render(request, 'blog/post_detail.html', {"post": post})


def posts_by_category(request, category_slug):
    # category = Category.objects.get(slug=category_slug)
    # posts = Post.objects.filter(category__slug=category_slug)
    category = get_object_or_404(Category, slug=category_slug)
    post_list = get_list_or_404(
        Post.objects.order_by("-id"), category=category)
    posts = helpers.pg_records(request, post_list)
    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'blog/post_by_category.html', context)


def posts_by_tag(request, tag_slug):
    # tag = Tag.objects.get(slug=tag_slug)
    # posts = Post.objects.filter(tags__name=tag)
    tag = get_object_or_404(Tag, slug=tag_slug)
    post_list = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    posts = helpers.pg_records(request, post_list)
    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, 'blog/post_by_tag.html', context)


def posts_by_author(request, author_name):
    # author = Author.objects.get(name=author_name)
    # posts = Post.objects.filter(author__name=author_name)
    user = get_object_or_404(auth.models.User, username=author_name)
    author = get_object_or_404(Author, user=user)
    post_list = get_list_or_404(Post.objects.order_by("-id"), author=author)
    posts = helpers.pg_records(request, post_list)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/post_by_author.html', context)


def feedback(request):
    if request.method == "POST":
        f = forms.FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(
                f.cleaned_data['subject'], f.cleaned_data['message'])
            try:
                mail_admins(subject, message)
                f.save()
                print("success")
                messages.add_message(
                    request, messages.SUCCESS, 'Feedback sent!')
            except Exception:
                print("failed")
                messages.add_message(request, messages.INFO,
                                     'Unable to send feedback. Try agian')

            return redirect('feedback')

    else:
        f = forms.FeedbackForm()

    return render(request, 'blog/feedback.html', {'form': f})


def test_cookie(request):
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue', max_age=5)
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))


def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse('Testing session cookie')


def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookie test passed")
    else:
        response = HttpResponse("Cookie test failed")

    return response


def save_session_data(request):
    request.session['id'] = 1
    request.session['name'] = 'root'
    request.session['password'] = 'rootpassword'

    return HttpResponse("Session Data Saved")


def access_session_data(request):
    response = ""
    if request.session.get('id'):
        response += "Id : {0} <br>".format(request.session.get('id'))
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(
            request.session.get('password'))

    if not response:
        return HttpResponse("No session data")
    else:
        return HttpResponse(response)


def delete_session_data(request):
    try:
        del request.session['id']
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass

    return HttpResponse("Session Data cleared")


def lousy_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'root' and password == 'pass':
            request.session['logged_in'] = True
            return redirect('lousy_secret')
        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'blog/lousy_login.html')


def lousy_secret(request):
    if not request.session.get('logged_in'):
        return redirect('lousy_login')

    return render(request, 'blog/lousy_secret_page.html')


def lousy_logout(request):
    try:
        del request.session['logged_in']
    except KeyError:
        return redirect('lousy_login')

    return render(request, 'blog/lousy_logout.html')


def login(request):
    if request.user.is_authenticated():
        return redirect('admin_page')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'blog/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'blog/logout.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('login')

    return render(request, 'blog/admin_page.html')
