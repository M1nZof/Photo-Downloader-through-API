import requests
import os
import argparse

from image_download import image_download
from dotenv import load_dotenv


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа загружает фото дня по версии NASA')
    parser.add_argument('-p', '--path', type=str,
                        help='Путь сохранения файлов. Стандартно - папка images')
    parser.add_argument('-n', '--number', type=int,
                        help='Количество фото. Стандартно - 30')
    args = parser.parse_args()    
    
    if args.path is None:
        path = 'images'
    else:
        path = args.path
    if args.number is None:
        number_of_photos = 30
    else:
        number_of_photos = args.number
        
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    payload = {
        'api_key': nasa_api_key,
        'count': number_of_photos
        }

    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    json_response = response.json()
    
    for index, image in enumerate(json_response):
        if image.get('hdurl'):
            image_link = image['hdurl']
            image_download(image_link, f'APOD_{index}', 'images')
      