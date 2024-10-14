import os, sys
from PIL import Image

img = Image.open('./assets/calm/Vagabond1.png')

base_width=1080

wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
img.save('somepic.png')