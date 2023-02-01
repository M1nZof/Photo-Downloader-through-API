import os
import telegram
import argparse

from random import shuffle
from dotenv import load_dotenv
from time import sleep


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа загружает фото в заданный телеграм-канал с заданным промежутком')
    parser.add_argument('-p', '--path', type=str,
                        help='Путь сохранения файлов. Стандартно - папка images')
    args = parser.parse_args()

    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    post_latency = int(os.environ['POST_LATENCY'])
    tg_channel = os.environ['TG_CHANNEL']
    bot = telegram.Bot(token=TG_TOKEN)

    if args.path:
        image_directory = os.walk(args.path)
    else:
        image_directory = os.walk('images')
    for dir_name, _, image in image_directory:
        image_list = image
    shuffle(image_list)    

    while True:
        for image in image_list:
            bot.send_photo(chat_id=TG_CHANNEL, photo=open(f'{dir_name}/{image}', 'rb'))
            sleep(post_latency)
            