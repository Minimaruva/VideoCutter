from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import random

def random_quote(file_path="./assets/Quotes.csv"):
    """Returns a random quote from quotes dataset"""
    
    quotes_df = pd.read_csv(file_path, sep=";")

    random_row = random.randint(1, len(quotes_df))

    quote = quotes_df.loc[random_row]["QUOTE"]

    return quote

def text_format(text_raw):
    """Formats text to fit on screen
    Return tuple (formatted text, line count)"""
    text = text_raw.replace("\n", "")
    text_arr = text.split(" ")
    line_count = 0

    if len(text) > 45:
        text = ""
        lines = [""]
        line_len = 0
        for i in text_arr:
            # Count length of each added line
            line_len += len(i) 
            if line_len >=40:
                # Add new element to the list representing new line
                line_count += 1
                lines.append(i+" ")
                line_len = len(i)
            else:
                # Add text to existing line
                lines[line_count] += i + " "

        # Get rid of whitespaces at the end of each line
        lines = [i[:-1] for i in lines]

        # Convert list to formatted text
        for i in lines:
            text += i+"\n"

        return (text, line_count)
    
    return (text, line_count)

def create_text_image(text="", font_size=50, text_position=(540, 75), text_color="black", bg_color="white", output_path="./assets/temp/quote_image.png"):
    """Creates a white box with specified quote
    Automatically adjusts size according to length of quote"""

    if text=="":
        text = random_quote()

    text_lines = text_format(text)
    text, lines = text_lines[0], text_lines[1]
    
    # Change height of rectangle according to text length
    if lines <= 2:
        width, length = 1080, (lines//2) * 150 + 150
    else:
        font_size -= 15
        width, length = 1080, (lines//2) * 75 + 150

    image_size = (width, length)

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

    img.save(output_path)
    return output_path

# quote = "what is the max length guys guys guys another gay even longer quote. OMG so long I barely how about even LOOOnger"

# create_text_image()
