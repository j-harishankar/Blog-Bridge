from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.signup, name='signup-page'),
    path('loginn/', views.loginn, name='login-page'),
    path('home/', views.home, name='home-page'),
    path('newpost/', views.newPost),
    path('mypost/', views.myPost ),
    
]
