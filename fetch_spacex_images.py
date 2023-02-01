import requests
import argparse

from image_download import image_download

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа загружает фото пусков ракет компании SpaceX')
    parser.add_argument('-p', '--path', type=str,
                        help='Путь сохранения файлов. Стандартно - папка images')
    parser.add_argument('-l', '--launch_id', type=str,
                        help='ID пуска. Стандартно - последний')                            
    args = parser.parse_args()
    
    if args.path is None:
        path = 'images'
    else:
        path = args.path
        
    if args.launch_id is None:
        launch_id = 'latest'
    else:
        launch_id = args.launch_id
    
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    
    response = requests.get(url)
    response.raise_for_status()
  
    result = response.json()
    result_links = result.get('links')
    result_flickr = result_links.get('flickr')
    images = result_flickr.get('original')

    if images:
      for index, image_link in enumerate(images):
        image_name = f'SpaceX_{index}'
        image_download(image_link, image_name, path)
    else:
      print('Увы, по данному запуску не было зафиксировано фото')
