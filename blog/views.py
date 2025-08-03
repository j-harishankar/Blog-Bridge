from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Post
# Create your views here.


def home(request):
    context = {'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)
def signup(request):
    return render(request, 'blog/signup.html')



def loginn(request):
    return render(request, 'blog/login.html')

