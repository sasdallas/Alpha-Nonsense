from django.contrib.auth.models import AbstractUser
from django.db import models
"""
class User(AbstractUser):
    pfp = models.CharField(default="https://nonsense.techdude17.repl.co/static/blank-pic.png")
    username = models.CharField(default="", max_length=64, blank=True)
    isLoggedIn = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "pfp": self.pfp,
            "username": self.username,
            "isLoggedIn": self.isLoggedIn,
            "upvotes": self.upvotes
        }"""