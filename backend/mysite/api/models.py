from django.db import models

# Create your models here.
class Bot(models.Model):
    userId = models.IntegerField()
    username = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    redditUsername = models.CharField(max_length=100)
    clientId = models.CharField(max_length=100)
    clientSecret = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    taskQueue = models.JSONField(default=dict)
