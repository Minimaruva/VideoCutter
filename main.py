from moviepy.editor import *

bg_path = "./assets/bg.png"
quote = "The world is simple"

bg = ImageClip(bg_path, duration=4).set_fps(30)

txt = TextClip(txt=quote).set_position(("center", "top"))


video = CompositeVideoClip([bg, txt])

video.write_videofile("./output/testvideo.mp4", codec="libx264")