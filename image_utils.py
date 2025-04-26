from PIL import Image
import os

def resize_image(image_path, target_width=1080, target_height=None, maintain_aspect_ratio=True):
    """
    Resize an image to target dimensions.
    If maintain_aspect_ratio is True and target_height is None, 
    height will be calculated to maintain the original aspect ratio.
    
    Returns: PIL Image object of the resized image
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Get original dimensions
        original_width, original_height = img.size
        
        if maintain_aspect_ratio and target_height is None:
            # Calculate height to maintain aspect ratio
            aspect_ratio = original_height / original_width
            target_height = int(target_width * aspect_ratio)
        
        # Resize the image
        resized_img = img.resize((target_width, target_height), Image.LANCZOS)
        return resized_img
        
    except Exception as e:
        print(f"Error resizing image: {e}")
        # Return the original image if resizing fails
        return Image.open(image_path)

def fit_to_frame(image_path, frame_width=1080, frame_height=1920):
    """
    Resize an image to fit within a frame while maintaining aspect ratio.
    The image will be resized so that it's fully contained within the frame.
    
    Returns: PIL Image object of the resized image
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Get original dimensions
        original_width, original_height = img.size
        
        # Calculate scaling factors
        width_ratio = frame_width / original_width
        height_ratio = frame_height / original_height
        
        # Use the smaller ratio to ensure the image fits within the frame
        scale_factor = min(width_ratio, height_ratio)
        
        # Calculate new dimensions
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        return resized_img
        
    except Exception as e:
        print(f"Error fitting image to frame: {e}")
        # Return the original image if resizing fails
        return Image.open(image_path)