from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Love)
admin.site.register(models.Comment)
admin.site.register(models.Flag)
admin.site.register(models.Follow)
admin.site.register(models.Post)