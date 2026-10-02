from PIL import Image
import requests

filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

def download(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)

download(filename, "reading_image_files/dog.jpg")
img = Image.open("reading_image_files/dog.jpg")
img.show()
