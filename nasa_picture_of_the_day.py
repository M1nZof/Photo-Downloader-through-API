import requests
from image_download import image_download
from dotenv import load_dotenv
import os

def nasa_picture_of_the_day():
  load_dotenv()
  API_KEY = os.environ['NASA_API_KEY']
  
  payload = {
    'api_key': API_KEY,
    'count': 30
  }
  
  url = 'https://api.nasa.gov/planetary/apod'
  response = requests.get(url, params=payload)
  response.raise_for_status()
  result = response.json()
  for index, image in enumerate(result):
    if image.get('hdurl'):
      image_link = image['hdurl']
      image_download(image_link, f'APOD_{index}', 'images')
      