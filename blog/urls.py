from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('test',views.test),
    path('loginn/', views.loginn, name='login-page'),

]
