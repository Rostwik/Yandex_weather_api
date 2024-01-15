import pytz
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from environs import Env
from datetime import timedelta

from yandex_weather_app.models import Town

env = Env()
env.read_env()

yandex_weather_key = env.str('YANDEX_WEATHER_API_KEY')


def sun(request):
    return render(request, "index.html")

    # try:
    #     if request.method == 'GET':
    #         town = {
    #             'name': 'СПб',
    #             'lat': 59.94,
    #             'lon': 30.31
    #         }
    #         yandex_api_url = 'https://api.weather.yandex.ru/v2/informers'
    #         headers = {
    #             'X-Yandex-API-Key': yandex_weather_key
    #         }
    #         payload = {
    #             'lat': town['lat'],
    #             'lon': town['lon'],
    #             'extra': 'false'
    #         }
    #         response = requests.get(yandex_api_url, params=payload, headers=headers)
    #         print(response)
    #         response.raise_for_status()
    #         weather_fact = response.json()['fact']
    #         print(weather_fact)
    #         weather_forecast = response.json()['forecast']
    #         print(weather_forecast)
    #
    #         return JsonResponse(
    #             {
    #                 'Город': town['name'],
    #                 'Температура': f"{weather_fact['temp']} градусов Цельсия",
    #                 'Атмосферное давление': f"{weather_fact['pressure_mm']} мм рт.ст.",
    #                 'Скорость ветра': f"{weather_fact['wind_speed']} м/с",
    #                 'sunrise': weather_forecast['sunrise'],
    #                 'sunset': weather_forecast['sunset']
    #             }
    #             , safe=False, json_dumps_params={
    #                 'ensure_ascii': False,
    #                 'indent': 4,
    #             })
    # except Exception as exp:
    #     print(exp)

def weather(request):
    if request.method == 'GET':
        current_tz = pytz.timezone('Europe/Moscow')
        timezone.activate(current_tz)
        try:
            town = Town.objects.get(name=request.GET['city'])
            if not town.is_request or town.request_time + timedelta(minutes=30) < timezone.localtime(timezone.now()):
                yandex_api_url = 'https://api.weather.yandex.ru/v2/forecast'
                headers = {
                    'X-Yandex-API-Key': yandex_weather_key
                }
                payload = {
                    'lat': town.lat,
                    'lon': town.lon,
                    'extra': 'false'
                }
                response = requests.get(yandex_api_url, params=payload, headers=headers)
                response.raise_for_status()
                weather_json = response.json()['fact']

                town.temp = weather_json['temp']
                town.pressure_mm = weather_json['pressure_mm']
                town.wind_speed = weather_json['wind_speed']
                town.is_request = True
                town.request_time = timezone.localtime(timezone.now())
                town.save()

            return JsonResponse(
                {
                    'Город': town.name,
                    'Температура': f'{town.temp} градусов Цельсия',
                    'Атмосферное давление': f'{town.pressure_mm} мм рт.ст.',
                    'Скорость ветра': f'{town.wind_speed} м/с'
                }
                , safe=False, json_dumps_params={
                    'ensure_ascii': False,
                    'indent': 4,
                })

        except Town.DoesNotExist:
            return JsonResponse(
                {'weather': 'Город не найден!'}
                , safe=False, json_dumps_params={
                    'ensure_ascii': False,
                    'indent': 4,
                })
