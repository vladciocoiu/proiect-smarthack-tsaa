# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Bot
from .models import Task

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ["userId", "name"]
        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name"]