from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.decorators import login_required
from . import models
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
@login_required(login_url='/loginn')
def home(request):
    context = {'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)

def signup(request):
    error_message = None

    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        if User.objects.filter(username=name).exists():
            error_message = "Username already taken"
        elif User.objects.filter(email=email).exists():
            error_message = "Email already registered"
        else:
            newUser = User.objects.create_user(username=name, email=email, password=password)
            newUser.save()
            return redirect('/loginn')

    return render(request, 'blog/signup.html', {'error': error_message})



def loginn(request):
    error_message = None 
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('home-page')
        else:
            error_message = "Invalid username or password"
    return render(request, 'blog/login.html', {'error': error_message})


@never_cache
@login_required(login_url='/loginn')
def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title = title,content=content,author=request.user)
        npost.save()
        return redirect('home-page')
    return render(request,'blog/newpost.html')

@never_cache
@login_required(login_url='/loginn')
def myPost(request):
    context = {'posts':Post.objects.filter(author = request.user)}
    return render(request,'blog/mypost.html',context)

@never_cache
@login_required(login_url='/loginn')
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id, author=request.user)  # Only get user's own post
    post.delete()
    return redirect('my-post')

def signOut(request):
    logout(request)
    return redirect('/loginn')