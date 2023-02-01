import requests
import os
import argparse

from image_download import image_download
from dotenv import load_dotenv


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа загружает фото дня по версии NASA')
    parser.add_argument('-p', '--path', type=str,
                        help='Путь сохранения файлов. Стандартно - папка images')
    args = parser.parse_args()    
    
    if args.path is None:
        path = 'images'
    else:
        path = args.path
        
    load_dotenv()
    API_KEY = os.environ['NASA_API_KEY']

    payload = {
        'api_key': API_KEY,
        'count': 30
        }

    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    json_response = response.json()
    
    for index, image in enumerate(json_response):
        if image.get('hdurl'):
            image_link = image['hdurl']
            image_download(image_link, f'APOD_{index}', 'images')
      