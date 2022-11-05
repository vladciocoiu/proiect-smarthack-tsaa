from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from .models import Bot
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import *


Bots = [Bot(0, userId=1, name="Bot1"), Bot(1, userId=1, name="Bot2")]
Tasks = []

@csrf_exempt
@api_view(['GET'])
def getBots(request):
    if(request.method == 'GET'):
        BotsDict = [model_to_dict(x) for x in Bots]
        BotsJson = json.dumps(BotsDict)
        return HttpResponse(BotsJson)

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
@api_view(['POST'])
def createBot(request):
    if(request.method == 'POST'):# create a new bot
        bot = Bot(len(Bots), userId=request.data.get('userId'), name=request.data.get('name'))
        Bots.append(bot)
        return HttpResponse("Bot created")
    #if(request.method == 'UPDATE'):

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
        