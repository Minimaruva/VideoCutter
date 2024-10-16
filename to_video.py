from moviepy.editor import *
from moviepy.video.fx.resize import resize
from quote_img import create_text_image
import os, sys
from PIL import Image

def img_resizer(img_path, base_width=1080):
    """Resize image to have same width as video"""

    img = Image.open(img_path)

    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))

    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    return img



def img_to_img(bg_path="./assets/bg.png", img_path="./assets/Calm/Vagabond1.jpg"):
    """Function that accepts input image to produce formatted image
    This is more efficient then producing a video out of image"""

