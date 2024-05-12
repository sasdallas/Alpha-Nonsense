from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from . import models
from .forms import PostForm
from datetime import datetime
import time
def welcome(request):
    return render(request, "welcome.html")

def login_view(request):
    if request.method == "POST":
        # Retrieve the username and password from the POST request

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html",
                         {"message": "Invalid username and/or password."})
    else:
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

@login_required
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print("Form is valid.")
            tt = round(time.time() * 1000)
            post = form.save(commit=False)
            post.tuser = request.user
            post.timestamp = datetime.now()
            post.pst_id = tt
            post.save()
            
    form = PostForm()
    return render(request, "index.html", {
        "user": request.user,
        "last":
        models.Post.objects.all().exclude(
            author=request.user.username).order_by('-id')[:20],
        "form": form
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("welcome"))

@login_required
def user_list(request):
    users = models.User.objects.exclude(username=request.user.username)
    return render(request, "users.html", {"users": users})
@login_required
def user(request, username):
    user = models.User.objects.get(username=username)
    print("Username: " + username)
    print("Got username: " + user.username)
    if request.method == "POST":
        print("Received POST request")
        current_user_profile = request.user
        print("User profile: " + current_user_profile.username)
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            print("Action was FOLLOW.")
            current_user_profile.follows.add(user)
            
        elif action == "unfollow":

            
            print("Action was UNFOLLOW.")
            current_user_profile.follows.remove(user)
        current_user_profile.save()
        
    return render(request, "user.html", {"user": user, "curuser": request.user})




# Why does this exist again?
def api(request, method):
    # We don't need a post method, Django forms handles that
    if method == "like":
        print("somebody tried to like something but we ignored it")


@login_required
def settings(request):
    if request.method == "POST":
        print("Received POST request")
    return render(request, "settings.html", {"user": request.user})

def like(request, id):
    post = models.Post.objects.get(pst_id=id)
    user = request.user
    print("Got username: " + user.username)
    try:
        like = models.Love.objects.get(post=post, user=user)
    
    except models.Love.DoesNotExist:
        print("User hasn't liked this post.")
        like = models.Love.objects.create(post=post, user=user)
        like.save()
        user.likes.add(like)
        post.userlikes.add(like)
        post.upvotes += 1
        post.save()
        user.save()
        return HttpResponseRedirect(reverse(index))
    
    print("Disliking post...")
    user.likes.remove(like)
    like.delete()
    post.upvotes -= 1
    post.userlikes.remove(like)
    post.save()
    user.save()
    
    return HttpResponseRedirect(reverse(index))