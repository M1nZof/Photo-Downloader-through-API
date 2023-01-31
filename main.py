import argparse
import telegram
import os

from time import sleep
from random import shuffle
from dotenv import load_dotenv

from fetch_spacex_images import fetch_spacex_last_launch
from nasa_epic import nasa_epic
from nasa_picture_of_the_day import nasa_picture_of_the_day


load_dotenv()
TG_TOKEN = os.environ['TG_TOKEN']
bot = telegram.Bot(token=TG_TOKEN)


image_directory = os.walk('images')
for dir_name, _, image in image_directory:
    image_list = image
    

shuffle(image_list)
for image in image_list:
    bot.send_photo(chat_id='@testttttttttttttasdasfsdf', photo=open(f'images/{image}', 'rb'))
    sleep(14400)


parser = argparse.ArgumentParser(description='Программа загружает фото запусков SpaceX, фото земли от NASA или фото дня от NASA')
parser.add_argument('search',
                    help='Что искать:'
                    '- sx - Фото от SpaceX. Если требуется, указать id пуска по аргументу -id. По стандарту это последний запуск; '
                    'epic - Фото земли от NASA; '
                    'apod - Фото дня от NASA;',
                    type=str
                   )
parser.add_argument('-id', help='ID вылета SpaceX', type=str)
parser.add_argument('-p', '--path', type=str,
                    help='Путь сохранения файлов. Стандартно - папка images')
args = parser.parse_args()

if args.search == 'sx':
  fetch_spacex_last_launch(args.path, args.id)
elif args.search == 'epic':
  nasa_epic()
elif args.search == 'apod':
  nasa_picture_of_the_day()
