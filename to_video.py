import os
from moviepy.editor import VideoClip, ImageClip, CompositeVideoClip, VideoFileClip
from moviepy.video.fx.resize import resize
from image_utils import fit_to_frame 
from PIL import Image

def img_to_img(quote_path, img_path, output_path="./output"):
    """
    Creates a static image combining the quote and input image
    quote_path: Path to the quote image
    img_path: Path to the background image
    output_path: Directory to save the output image
    """
    try:

        os.makedirs(output_path, exist_ok=True)
        
        # Load the photo and quote as PIL images
        
        
        # Open background image
        background = Image.open(img_path)
        
        # Resize quote image to fit within background width
        quote_img = fit_to_frame(quote_path, frame_width=background.width - 40, frame_height=background.height)
        
        # Create new canvas to place quote above the image with spacing
        margin = 20
        canvas_width = background.width
        canvas_height = quote_img.height + background.height + 2 * margin
        combined = Image.new('RGB', (canvas_width, canvas_height), color=(255,255,255))
        
        # Paste quote at top with margin
        qx = (canvas_width - quote_img.width) // 2
        combined.paste(quote_img, (qx, margin), quote_img if quote_img.mode == 'RGBA' else None)
        
        # Paste background below quote with margin
        combined.paste(background, (0, quote_img.height + margin))
        
        # Save the result
        output_file = os.path.join(output_path, "combined_image.png")
        combined.save(output_file)
        
        return output_file
    except Exception as e:
        print(f"Error in img_to_img: {e}")
        raise

def img_to_video(quote_path, duration=10, img_path=None, output_path="./output"):
    """
    Creates a video with static image and quote
    quote_path: Path to the quote image
    duration: Duration of the video in seconds
    img_path: Path to the background image
    output_path: Directory to save the output video
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_path, exist_ok=True)
        
        # Load the background image
        bg_clip = ImageClip(img_path).set_duration(duration).set_fps(1)
        
        # Load quote image
        quote_clip = ImageClip(img=quote_path).set_position(("center", "top")).set_duration(duration)
        
        # Combine clips
        video = CompositeVideoClip([bg_clip, quote_clip])
        
        # Save the video
        output_file = os.path.join(output_path, "output_video.mp4") 
        video.write_videofile(output_file, codec="libx264")
        
        return output_file
    except Exception as e:
        print(f"Error in img_to_video: {e}")
        raise

def video_to_video(quote_path, duration=None, video_path=None, output_path="./output"):
    """
    Overlays quote on an existing video

    quote_path: Path to the quote image
    duration: Duration to trim the video to (uses full video if None)
    video_path: Path to the input video
    output_path: Directory to save the output video
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_path, exist_ok=True)
        
        # Load the video
        video_clip = VideoFileClip(video_path)
        
        # Set duration if specified
        if duration is not None:
            video_clip = video_clip.subclip(0, min(duration, video_clip.duration))
        
        # Load quote image
        quote_clip = ImageClip(img=quote_path).set_position(("center", "top")).set_duration(video_clip.duration)
        
        # Combine clips
        final_video = CompositeVideoClip([video_clip, quote_clip])
        
        # Save the video
        output_file = os.path.join(output_path, "output_video.mp4")
        final_video.write_videofile(output_file, codec="libx264")
        
        return output_file
    except Exception as e:
        print(f"Error in video_to_video: {e}")
        raise