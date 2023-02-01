import requests
import os


def get_picture_format(picture):
    _, file_format = os.path.splitext(picture)
    return file_format


def image_download(url, filename, path, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    file_format = get_picture_format(url)

    if not os.path.exists(path):
        os.mkdir(path)

    image_path = os.path.join(path, (filename + file_format))
    with open(image_path, 'wb') as file:
        file.write(response.content)
    