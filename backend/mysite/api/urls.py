from django.urls import path

from . import views

urlpatterns = [
    path('bots', views.bots, name='bots'),
    path('bots/<int:botId>', views.bot, name='bot'),
    path('bots/<int:botId>/tasks', views.getTasks, name='tasks'),
    path('bots/<int:botId>/tasks/<int:taskId>', views.task, name='task'),
]