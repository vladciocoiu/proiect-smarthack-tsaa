from django.db import models

# Create your models here.
class Bot(models.Model):
    userId = models.IntegerField()
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    

class Task(models.Model):
    botId = models.IntegerField()
    name = models.CharField(max_length=100)
    params = models.JSONField()

