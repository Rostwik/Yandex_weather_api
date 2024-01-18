from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from yandex_weather_app import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('sun/', views.sun, name='sun'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
