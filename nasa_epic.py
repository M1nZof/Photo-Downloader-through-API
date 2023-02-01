import requests
import os
import argparse

from image_download import image_download
from dotenv import load_dotenv


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа загружает фото Земли сделанные NASA')
    parser.add_argument('-p', '--path', type=str,
                        help='Путь сохранения файлов. Стандартно - папка images')
    args = parser.parse_args()
    
    if args.path is None:
        path = 'images'
    else:
        path = args.path
    
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_api_key}

    response = requests.get(url, params=payload)
    response.raise_for_status()
    json_response = response.json()
  
    for index, picture in enumerate(json_response):
        picture_name = f"{picture['image']}.png"
        picture_datetime = picture['date']
        picture_date = picture_datetime.split()[0].split('-')
        year, month, day = picture_date
        day, month, year = day, month, year
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{str(year)}/{str(month)}/{str(day)}/png/{picture_name}"
        image_download(image_url, f'EPIC_{index}', 'images', payload)
