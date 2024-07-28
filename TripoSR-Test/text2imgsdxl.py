import replicate
from dotenv import load_dotenv
from pprint import pprint 
import requests


load_dotenv()

def download_image(image_url, filename):
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print("Failure!!!")

output = replicate.run(
  "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",
  input={"prompt": "An astronaut riding a rainbow unicorn, cinematic, dramatic"}
)

pprint(output)
download_image(output[0], "output.jpg")

