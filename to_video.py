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



def img_to_img(quote_path, bg_path="./assets/bg.png", img_path="./assets/Calm/Vagabond1.jpg", output_path="./output"):
    """Function that accepts input image to produces formatted image
    This is more efficient then producing a video out of image"""
    
    try:
        bg = Image.open(bg_path)
    except:
        bg = Image.new("RGB", (1080, 1920), "black")
    
    # img = Image.open(img_path)
    img = img_resizer(img_path)
    quote = Image.open(quote_path)

    bg.paste(img, (0,quote.size[1]))
    bg.paste(quote, (0,0))

    bg.save(output_path+"/output_img.png")
    return output_path+"/output_img.png"

def img_to_video(quote_path, duration=0, fps=30, bg_path="./assets/bg.png", img_path="./assets/Calm/Vagabond1.jpg", output_path="./output"):
    """Function that accepts input image to produce formatted image
    in a form of a video of specified duration"""
    
    # bg = ImageClip(bg_path, duration=4)
    # quote_clip = ImageClip(img=quote).set_position(("center", "top")).set_duration(duration)
    # img_clip = ImageClip(img=img_path).set_position("center").set_duration(duration)
    image_clip = ImageClip(img=img_to_img(quote_path, bg_path=bg_path, img_path=img_path)).set_duration(duration)

    video = CompositeVideoClip([image_clip])

    try:
        video.write_videofile(output_path+"/outputvideo.mp4", codec="libx264", threads = 8, fps=fps)
    except:
        video.write_videofile(output_path+"/outputvideo.mp4", codec="libx264", fps=fps)
    return None

def video_to_video(quote_path, duration=0, bg_path="./assets/bg.png", video_path="./assets/Sad/Sad1.mp4", output_path="./output"):
    """Function that accepts quote and video as input
    to save formatted video to specified folder"""
    quote_img = Image.open(quote_path)
    d_from_top = quote_img.size[1]

    bg = ImageClip(bg_path)
    video_clip = VideoFileClip(video_path,).set_position(("center", d_from_top))
    quote_clip = ImageClip(quote_path).set_position(("center", "top"))

    if duration == 0:
        video = CompositeVideoClip([bg, quote_clip, video_clip]).set_duration(video_clip.duration)
    else:
        video = CompositeVideoClip([bg, quote_clip, video_clip]).set_duration(duration)

    try:
        video.write_videofile(output_path+"/outputvideo.mp4", codec="libx264", threads = 8)
    except:
        video.write_videofile(output_path+"/outputvideo.mp4", codec="libx264")
    return None

# quote = create_text_image("The text is ojbogjbijr long. Try again latter cuz its veryyyyyyy looong")

# img_to_img(quote_path=quote, output_path="C:/Users/agnen/OneDrive/Desktop/HSO")
# img_to_video(quote)
# video_to_video(quote)