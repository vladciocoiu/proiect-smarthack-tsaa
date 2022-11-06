from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from .models import Bot
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
import json
from django.views.decorators.csrf import csrf_exempt
from .taskRunner.taskRunner import taskRunner
from .taskRunner.taskRunner import Bots
import threading


# username = "tsaaaaaaaa"
# password = "parola123"
# client_id = "23bQR7XTzbODBmXw2WQHlg"
# client_secret = "Qm8T8hV2SjHmdQGUYk6gKz5NZbT19w"

_taskRunner = taskRunner()

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
    if(request.method == 'PUT'):# create a new bot
        print(request.data)
        bot = Bot(
            botId, 
            userId=1,
            username=request.data.get('username'),
            active=request.data.get('active'),
            redditUsername=request.data.get('redditUsername'),
            clientId=request.data.get('clientId'),
            clientSecret=request.data.get('clientSecret'),
            password=request.data.get('password'),
            taskQueue=request.data.get('taskQueue')
            )
        Bots[botId] = bot
        botDict = model_to_dict(bot)
        botJson = json.dumps(botDict)
        return HttpResponse(botJson)
        
@csrf_exempt
@api_view(['GET'])
def start(request):
    if(request.method == 'GET'):
        if(_taskRunner.started == False):
            _taskRunner.start()
            threading.Thread(target=_taskRunner.run()).start()
        print("start called")
        return HttpResponse("Bot started")

@csrf_exempt
@api_view(['GET'])
def stop(request):
    if(request.method == 'GET'):
        _taskRunner.stop()
        return HttpResponse("Bot stopped")
