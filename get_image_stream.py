import shutil
import requests, sys
from PIL import Image

image_link = sys.argv[1]
response = requests.get(image_link, stream=True)
#with open('image', 'wb') as file:
#    shutil.copyfileobj(response.raw, file)
#del response

#r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if response.status_code == 200:
    with open('image.jpeg', 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)


#image = Image.open('image.jpg')
# The file format of the source file.
#print(image.format)

# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
#print(image.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
#print(image.size) # Output: (1200, 776)

# Colour palette table, if any.
#print(image.palette) # Output: None