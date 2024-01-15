from django.urls import path
from django.shortcuts import render

from yandex_weather_app import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('sun/', render, kwargs={'template_name': 'index.html'}, name='sun_page'),
]
