"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.shortcuts import render, redirect
from django.contrib import messages, admin
from django.urls import path
from django.conf import settings
from django.http import HttpResponseRedirect
from . import views
import random

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path("index", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("users", views.user_list, name="users"),
    path("user/<str:username>", views.user, name="user"),
    path("api/<str:method>", views.api, name="api"),
    path("settings", views.settings, name="settings"),
    path("like/<int:id>", views.like, name="like")
]
