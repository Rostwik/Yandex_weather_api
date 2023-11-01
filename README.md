# Yandex weather

The application allows you to find out the weather in a certain city. The project provides two use cases - API based on Django library or via telegram-bot.
The application uses the [Yandex Weather API service](https://yandex.ru/dev/weather/doc/dg/concepts/about.html)
There is also a command to automatically fill in the database from a file or clear the table with cities.

## Enviroments

Сreate the file .env and fill in this data.

To work with django api:
- DEBUG
- SECRET_KEY
- ALLOWED_HOSTS
- YANDEX_WEATHER_API_KEY

To work with telegram-bot:
- Create new bot in Telegram and get the token   
  (you can obtain bot from @BotFather in Telegram, [See example](https://telegra.ph/Awesome-Telegram-Bot-11-11))
- TELEGRAM_API_TOKEN
- YANDEX_WEATHER_API_KEY
  
## Installing

To get started go to terminal(mac os) or CMD (Windows)
- create virtualenv, [See example](https://python-scripts.com/virtualenv)

- clone github repository or download the code

```bash
$git clone https://github.com/Rostwik/Yandex_weather_api.git
```

- install packages

```bash
$pip install -r requirements.txt
```
run the API Django 
```bash
$python manage.py runserver
```
run telegram-bot
```bash
$python manage.py weather_bot
```

delete all towns in db
```bash
$python manage.py delete_all_towns
```


load towns in db from towns_coordinates.txt (see in django_yandex_weather directory)
```bash
$python manage.py load_towns
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


