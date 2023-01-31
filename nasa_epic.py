import requests
from image_download import image_download
from dotenv import load_dotenv
import os


def nasa_epic():
  load_dotenv()
  API_KEY = os.environ['NASA_API_KEY']
  
  url = 'https://api.nasa.gov/EPIC/api/natural/images'
  payload = {'api_key': API_KEY}
  
  response = requests.get(url, params=payload)
  response.raise_for_status()
  result = response.json()
  
  for index, picture in enumerate(result):
    picture_name = picture['image'] + '.png'
    picture_datetime = picture['date']
    picture_date = picture_datetime.split()[0].split('-')
    year, month, day = picture_date
    day, month, year = day, month, year
    image_url = f"https://api.nasa.gov/EPIC/archive/natural/{str(year)}/{str(month)}/{str(day)}/png/{picture_name}"
    image_download(image_url, f'EPIC_{index}', 'images', payload)
    