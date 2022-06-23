from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator

from .models import Post


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'register.html', {'user': request.user})

    posts = Post.objects.filter(author=request.user).order_by("-id")

    return render(request, 'homepage.html', {'posts': posts})


def account_register(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'register.html', {'user': request.user})
        else:
            return redirect('/')
    else:
        user_email = request.POST.get('email')
        user_name = request.POST.get('username')
        user_pass = request.POST.get('pass')

        user = User.objects.create_user(user_name, user_email, user_pass)
        user.save()
        return redirect('/')
    
    
def account_auth(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'signin.html')
        else:
            return redirect('/')
    else:
        user_name = request.POST.get('username')
        user_pass = request.POST.get('pass')

        user = authenticate(request, username=user_name, password=user_pass)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/auth')


def account_logout(request):
    logout(request)
    return redirect('/')


def account_settings(request):
    pass


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    if request.method == 'GET':
        print(request)
        return render(request, 'post.html', {'title': 'Title', 'body': 'My new post'})
    else:
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')
        post = Post.objects.create(title=post_title, body=post_text, author=request.user)
        return redirect(f"/{request.user}/{str(post.random_url_id)}")


def post_get_or_save(request, post_url, user_name):
    if request.method == 'GET':
        post = Post.objects.get(random_url_id=post_url)
        return render(request, 'post.html', {'title': post.title, 'body': post.body})

    post = Post.objects.filter(random_url_id=post_url)
    if request.user.id == post.get().author_id:
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')
        post.update(title=post_title, body=post_text)
        return redirect(f"/{request.user}/{post_url}")
    else:
        return redirect('/')
