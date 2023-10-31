from django.db import models


class Town(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name='Название города')
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    temp = models.IntegerField(verbose_name='Температура', blank=True, null=True)
    wind_speed = models.IntegerField(verbose_name='Скорость ветра', blank=True, null=True)
    pressure_mm = models.IntegerField(verbose_name='Давление', blank=True, null=True)
    request_time = models.DateTimeField(verbose_name='Время запроса', blank=True, null=True)
    is_request = models.BooleanField(verbose_name='Наличие запроса', blank=True, null=True)

    def __str__(self):
        return self.Name
