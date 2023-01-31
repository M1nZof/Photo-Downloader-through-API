import requests
from image_download import image_download

def fetch_spacex_last_launch(path='images', launch_id='latest'):
  if path is None:
    path = 'images'
  if launch_id is None:
    launch_id = 'latest'
    
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
