from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from .models import Bot
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
import json
from django.views.decorators.csrf import csrf_exempt


Bots = [
    Bot(
        0,
        userId = 1,
        username = "test",
        active = True,
        redditUsername = "test",
        clientId = "test",
        clientSecret = "test",
        password = "test",
        Task = {"Type": "reply", "params": {"subreddit": "test", "keywords": ["test"], "message": "test"}}
    ),
    Bot(
        1,
        userId = 1,
        username = "test2",
        active = True,
        redditUsername = "test2",
        clientId = "test2",
        clientSecret = "test2",
        password = "test2",
        Task = {"Type": "reply", "params": {"subreddit": "test2", "keywords": ["test2"], "message": "test2"}}
    )

]

@csrf_exempt
@api_view(['GET', 'POST'])
def bots(request):
    if(request.method == 'GET'):
        BotsDict = [model_to_dict(x) for x in Bots]
        BotsJson = json.dumps(BotsDict)
        return HttpResponse(BotsJson)
    if(request.method == 'POST'):# create a new bot
        print(request.data)
        bot = Bot(len(Bots), 
        userId=1,
        username=request.data.get('username'),
        redditUsername=request.data.get('redditUsername'),
        clientId=request.data.get('clientId'),
        clientSecret=request.data.get('clientSecret'),
        password=request.data.get('password')
        )
        Bots.append(bot)
        botDict = model_to_dict(bot)
        botJson = json.dumps(botDict)
        return HttpResponse(botJson)
    

@csrf_exempt
@api_view(['GET', 'DELETE', 'PUT'])
def bot(request, botId):
    if(request.method == 'GET'):# return the bot with id = botId
        bot = Bots[botId]
        botDict = model_to_dict(bot)
        botJson = json.dumps(botDict)
        return HttpResponse(botJson)
    if(request.method == 'DELETE'):
        bot = Bots.pop(botId)
        botDict = model_to_dict(bot)
        botJson = json.dumps(botDict)
        return HttpResponse("Bot deleted")
    if(request.method == 'PUT'):
        bot = Bots[botId]
        bot.name = request.data.get('name')
        bot.userId = request.data.get('userId')
        botDict = model_to_dict(bot)
        botJson = json.dumps(botDict)
        return HttpResponse("Bot updated")


@csrf_exempt
@api_view(['GET'])
def getTasks(request, botId):
    if(request.method == 'GET'):
        TasksDict = [model_to_dict(x) for x in Tasks]
        TasksJson = json.dumps(TasksDict)
        return HttpResponse(TasksJson)

@csrf_exempt
@api_view(['GET', 'DELETE', 'PUT'])
def task(request, botId, taskId):
    if(request.method == 'GET'):
        task = Tasks[taskId]
        taskDict = model_to_dict(task)
        taskJson = json.dumps(taskDict)
        return HttpResponse(taskJson)
    if(request.method == 'DELETE'):
        task = Tasks.pop(taskId)
        taskDict = model_to_dict(task)
        taskJson = json.dumps(taskDict)
        return HttpResponse("Task deleted")
    if(request.method == 'PUT'):
        task = Tasks[taskId]
        task.name = request.data.get('name')
        task.params = request.data.get('params')
        taskDict = model_to_dict(task)
        taskJson = json.dumps(taskDict)
        return HttpResponse("Task updated")
        