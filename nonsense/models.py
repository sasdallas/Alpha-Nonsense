from django.contrib.auth.models import AbstractUser
from django.db import models


class Love(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, default=97)
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=1)
    author = models.CharField(default="", max_length=64)


class Post(models.Model):
    tuser = models.ForeignKey("User",
                              related_name="posts",
                              on_delete=models.CASCADE,
                              default=1)
    author = models.CharField(default="", max_length=100)
    timestamp = models.CharField(default="2021-04-24 00:36:14", max_length=100)
    md = models.CharField(default="", max_length=1000)
    pst_id = models.IntegerField(default=97)
    upvotes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    flags = models.IntegerField(default=0)

    userlikes = models.ManyToManyField("Love", blank=True, related_name="+")

    def serialize(self):
        return {
            "user": User.serialize(),
            "html": self.html,
            "md": self.md,
            "pst_id": self.pst_id,
            "upvotes": self.upvotes,
        }


class User(AbstractUser):
    pfp = models.CharField(
        default="https://nonsense.techdude17.repl.co/static/blank-pic.png",
        max_length=1000)
    username = models.CharField(default="",
                                max_length=64,
                                blank=True,
                                unique=True)
    isLoggedIn = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)

    likes = models.ManyToManyField("Post", blank=True, related_name="+")

    # This is a settings option, used to change whether the feed displays followed or default
    feedOption = models.CharField(default="d", max_length=2)

    def serialize(self):
        return {
            "pfp": self.pfp,
            "username": self.username,
            "isLoggedIn": self.isLoggedIn,
            "upvotes": self.upvotes
        }


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, default=97)
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=1)
    author = models.CharField(default="", max_length=64)
    content = models.CharField(default="error", max_length=100000)


class Flag(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, default=97)
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=1)
    author = models.CharField(default="", max_length=64)


class Follow(models.Model):
    following = models.ForeignKey("User",
                                  on_delete=models.CASCADE,
                                  default=1,
                                  related_name="following")
    follower = models.ForeignKey("User",
                                 on_delete=models.CASCADE,
                                 default=1,
                                 related_name="follower")
