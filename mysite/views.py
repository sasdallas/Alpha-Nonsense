"""from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from . import models
def welcome(request):
    return render(request, "welcome.html")

def login_view(request):
    return render(request, "login.html")
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if len(username.split()) > 1:
            return render(request, "register.html", 
                          {"message": "Error: Your username must be one word."})

        try:
            # Create the user
            user = models.User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html",
                         {"message": "Error: That username is already taken."})
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
        
    else: 
        return render(request, "register.html")


def index(request):
    return render(request, "temp.html")"""