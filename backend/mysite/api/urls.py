from django.urls import path

from . import views

urlpatterns = [
    path('bots', views.getBots, name='bots'),
    path('bot/<int:botId>', views.bot, name='bot'),
    path('bot', views.createBot, name='createBot'),
]