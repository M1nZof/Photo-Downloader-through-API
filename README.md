# Photo-Downloader-through-API

Скрипт по получению и отправке фото на космическую тематику на канал в TG

## Настройка окружения .env

Переменные окружения с примером:

- NASA_API_KEY - [API ключ от NASA](https://api.nasa.gov/);
- TG_TOKEN - Токен от TG-бота. Получается у [@BotFather](https://t.me/BotFather);
- POST_LATENCY - Задержка в отправке постов в группе (указывается в секундах)
- TG_CHANNEL - В какой канал отравляются посты

```
NASA_API_KEY=aAgG24Ss
TG_TOKEN=123123:AaBbCc
POST_LATENCY=14400
TG_CHANNEL=@test (or id of channel)
```

## Как пользоваться скриптом

Запуск через командную строку командой
```
python script_name.py -argument argument_value
```

Аргументы:

- `-h` - вывод справки;
- `-p` - желаемый путь для сохранения фото. По умолчанию - images в папке с исполняемым файлом;
- `-l` - ID запуска SpaceX
