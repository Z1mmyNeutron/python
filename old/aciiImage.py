from PIL import Image
imName = "dickbutt.png"
with Image.open(imName) as image:
    width, height = 640, 480
try:
    img = Image.open("dickbutt.png")
except IOError:
    pass