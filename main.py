from moviepy.editor import *
from moviepy.video.fx.resize import resize
from quote_img import create_text_image

bg_path = "./assets/bg.png"
quote = create_text_image(text="Trying out long quote bla bla bla. Like really long quote for real man")

#Open photo, convert it to avoid error
photo = "./assets/somepic.png"

def img_combine():
    """Combines quote image with desired image"""

def vid_combine():
    """Combines quote image with desired video"""

bg = ImageClip(bg_path, duration=4).set_fps(30)

quote_clip = ImageClip(img=quote).set_position(("center", "top")).set_duration(4)

photo_clip = ImageClip(img=photo).set_position("center").set_duration(4)

video = CompositeVideoClip([bg, photo_clip, quote_clip])

video.write_videofile("./output/testvideo.mp4", codec="libx264")