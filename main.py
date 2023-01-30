import requests
import os


def get_picture_format(picture):
  _, file_format = os.path.splitext(picture)
  return file_format


def image_download(url, path, filename, payload=None):
  if payload:
    response = requests.get(url, params=payload)
  else:
    response = requests.get(url)
  response.raise_for_status()
  file_format = get_picture_format(url)

  if not os.path.exists(path):
    os.mkdir(path)

  image_path = os.path.join(path, (filename + file_format))
  with open(image_path, 'wb') as file:
    file.write(response.content)


def fetch_spacex_last_launch(path, filename):
  url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    
  response = requests.get(url)
  response.raise_for_status()
  
  result = response.json()
  images = result['links']['flickr']['original']
  
  for index, image_link in enumerate(images):
    image_name = f'{filename}_{index}'
    image_download(image_link, 'images', image_name)


def nasa_picture_of_the_day(path):
  payload = {
    'api_key': 'rRG3bcsRVn1GZSwVBdiQmk7E208pbQ07yWhia1jN',
    'count': 30
  }
  url = 'https://api.nasa.gov/planetary/apod'
  response = requests.get(url, params=payload)
  response.raise_for_status()
  result = response.json()
  for index, image in enumerate(result):
    if image.get('hdurl'):
      image_link = image['hdurl']
      image_download(image_link, 'images', f'APOD_{index}')
  

def nasa_epic():
  url = 'https://api.nasa.gov/EPIC/api/natural/images'
  payload = {'api_key': 'rRG3bcsRVn1GZSwVBdiQmk7E208pbQ07yWhia1jN'}
  response = requests.get(url, params=payload)
  response.raise_for_status()
  result = response.json()
  for index, picture in enumerate(result):
    picture_name = picture['image'] + '.png'
    picture_datetime = picture['date']
    picture_date = picture_datetime.split()[0].split('-')
    year, month, day = picture_date
    day, month, year = day, month, year
    # image_url = os.path.join('https://api.nasa.gov/EPIC/archive/natural/', str(year), str(month), str(day), 'png', picture_name)
    image_url = f"https://api.nasa.gov/EPIC/archive/natural/{str(year)}/{str(month)}/{str(day)}/png/{picture_name}"
    image_download(image_url, 'images', f'EPIC_{index}', payload)
    

# url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
# image_dir_name = 'images'
# image_download(url, image_dir_name, 'hubble')

# img_dir = 'images'
# fetch_spacex_last_launch(img_dir, 'spacex')

# nasa_picture_of_the_day('images')

nasa_epic()
