import requests
import argparse

from image_download import image_download

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа загружает фото пусков ракет компании SpaceX')
    parser.add_argument('-p', '--path', type=str, default='images',
                        help='Путь сохранения файлов. Стандартно - папка images')
    parser.add_argument('-l', '--launch_id', type=str, default='latest',
                        help='ID пуска. Стандартно - последний')                            
    args = parser.parse_args()
    
    url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'
    
    response = requests.get(url)
    response.raise_for_status()

    response_links = response.json().get('links')
    response_flickr = response_links.get('flickr')
    images = response_flickr.get('original')

    if images:
        for index, image_link in enumerate(images):
            image_name = f'SpaceX_{index}'
            image_download(image_link, image_name, args.path)
