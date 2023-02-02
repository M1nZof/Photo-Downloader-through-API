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
- `-n` - количество фотографий для загрузки
- `-l` - ID запуска SpaceX

### Примеры:

1. Загрузка фото пусков SpaceX в папку `images` с ID запуска `5eb87d46ffd86e000604b388`

```
python fetch_spacex_images.py -p images -l 5eb87d46ffd86e000604b388
```

2. Загрузка фото Земли от NASA в папку `images`

```
python nasa_epic.py -p images
```

3. Загрузка 10 фотографий дня по версии NASA в папку `images`

```
python nasa_picture_of_the_day.py -p images -n 10
```

4. Автоматическая отправка постов с фотографиями из папки `images` 

```
python tg_send_post.py -p images
```
