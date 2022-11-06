from django.urls import path

from . import views

urlpatterns = [
    path('bots', views.bots, name='bots'),
    path('bots/<int:botId>', views.bot, name='bot'),
    path('start', views.start, name='start'),
    path('stop', views.stop, name='stop')
]