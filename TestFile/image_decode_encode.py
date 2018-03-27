import base64
from PIL import Image

image_read = Image.open('tum.jpg')
print(image_read)
"""
image_64_encode = base64.encodestring(image_read)
print(image_64_encode)
image_64_decode = base64.decodestring(image_64_encode) 
print(image_64_decode)
print(image_read.size)
img = Image.frombytes('RGB', (180,218), image_64_decode)
print(img)"""