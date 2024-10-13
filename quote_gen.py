from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, font_size=50, image_size=(1080, 150), text_position=(540, 75), text_color="black", bg_color="white", output_path="./assets/temp/quote_image.png"):

    # Create a new image with the specified background color
    img = Image.new("RGB", image_size, color=bg_color)
    d = ImageDraw.Draw(img)
    
    # Load a font, using a default fallback if not found
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text_bbox = d.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate the position to center the text
    text_x = (image_size[0] - text_width) / 2
    text_y = (image_size[1] - text_height) / 2

    # Add the text to the image at the calculated position
    d.text((text_x, text_y), text, font=font, fill=text_color)

    # Save the image to the specified output path
    img.save(output_path)
    return output_path

create_text_image(text="quote bla bla")