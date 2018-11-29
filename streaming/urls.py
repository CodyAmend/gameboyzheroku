from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

app_name = 'streaming'

urlpatterns = [

    path('Videos/<slug:slug>/', views.Streaming, name='streams'),
    path('StreamLanding', views.Streaming_Landing, name='game_videos'),

]