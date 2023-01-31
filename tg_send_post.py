import os

from random import shuffle


def tg_send_post(bot, channel):
    image_directory = os.walk('images')
    for dir_name, _, image in image_directory:
        image_list = image
    shuffle(image_list)    

    while True:
        for image in image_list:
            bot.send_photo(chat_id=channel, photo=open(f'images/{image}', 'rb'))
            sleep(LATENCY)