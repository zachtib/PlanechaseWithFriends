from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<str:game_id>/', views.room, name='room'),
]
