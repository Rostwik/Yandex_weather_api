from django.http import JsonResponse
from environs import Env

env = Env()
env.read_env()

YANDEX_WEATHER_KEY = env.str('YANDEX_WEATHER_API_KEY')


def weather(request):
    if request.method == 'GET':
        return JsonResponse(
            {'weather': 'Погода'}
            , safe=False, json_dumps_params={
                'ensure_ascii': False,
                'indent': 4,
            })
