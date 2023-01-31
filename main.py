import argparse
import telegram
import os

from time import sleep
from random import shuffle
from dotenv import load_dotenv

from fetch_spacex_images import fetch_spacex_last_launch
from nasa_epic import nasa_epic
from nasa_picture_of_the_day import nasa_picture_of_the_day
from tg_send_post import tg_send_post

if __name__ == '__main__':
    load_dotenv()
    TG_TOKEN = os.environ['TG_TOKEN']
    LATENCY = int(os.environ['LATENCY'])
    CHANNEL = os.environ['CHANNEL']
    bot = telegram.Bot(token=TG_TOKEN)
    
    parser = argparse.ArgumentParser(description='Программа загружает фото запусков SpaceX, фото земли от NASA или фото дня от NASA')
    parser.add_argument('action',
                    help='Что делать:'
                    'sx - Фото от SpaceX. Если требуется, указать id пуска по аргументу -id. По стандарту это последний запуск; '
                    'epic - Фото земли от NASA; '
                    'apod - Фото дня от NASA; '
                    'tg - Отправлять фото в tg-канал.',
                    type=str
                   )
    parser.add_argument('-id', help='ID вылета SpaceX', type=str)
    parser.add_argument('-p', '--path', type=str,
                        help='Путь сохранения файлов. Стандартно - папка images')
    args = parser.parse_args()

    if args.action == 'sx':
        fetch_spacex_last_launch(args.path, args.id)
    elif args.action == 'epic':
        nasa_epic()
    elif args.action == 'apod':
        nasa_picture_of_the_day()
    elif args.action == 'tg':
        tg_send_post(bot, CHANNEL)
