from moviepy.editor import *
from moviepy.video.fx.resize import resize
from quote_img import create_text_image
import os, sys
from PIL import Image
from quote_img import create_text_image


def img_resizer(img_path, base_width=1080):
    """Resize image to have same width as video"""

    img = Image.open(img_path)

    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))

    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    return img



def img_to_img(quote_path, img_path="./assets/Calm/Vagabond1.jpg", output_path="./output"):
    """Function that accepts input image to produce formatted image
    This is more efficient then producing a video out of image"""
    
    # Create a black background
    bg = Image.new("RGB", (1080, 1920), "black")

    img = Image.open(img_path)
    quote = Image.open(quote_path)

    bg.paste(img, (0,250))
    bg.paste(quote, (0,0))

    bg.save("./output/output_img.png")

quote = create_text_image(text="Trying out long quote bla bla bla. Like really long quote for real man")

img_to_img(quote_path=quote)