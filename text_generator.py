from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import random
import os

def random_quote(file_path="./assets/Quotes.csv", max_length=100):
    """Returns a random quote from quotes dataset, filtered by max_length."""
    try:
        if not os.path.exists(file_path):
            print(f"Quote file not found: {file_path}")
            return "No quotes available. File not found."

        quotes_df = pd.read_csv(file_path, sep=";")

        if len(quotes_df) == 0:
            return "No quotes available. Empty file."

        # Filter quotes by length
        filtered_quotes = quotes_df[quotes_df["QUOTE"].str.len() <= max_length]

        if len(filtered_quotes) == 0:
            return f"No quotes available under {max_length} characters."

        # Select a random row from the filtered DataFrame
        # Use .sample() for potentially better random selection on indices after filtering
        random_quote_series = filtered_quotes.sample(n=1).iloc[0]
        quote = random_quote_series["QUOTE"]

        return quote
    except Exception as e:
        print(f"Error retrieving random quote: {e}")
        return "Error loading quotes."

def text_format(text_raw, max_chars_per_line=40):
    """Formats text to fit within a specified character width per line.
    Return tuple (formatted text, line count)"""
    if not text_raw:
        return ("", 0)

    text = text_raw.replace("\n", " ").strip()

    # Handle empty text
    if not text:
        return ("", 0)

    text_arr = text.split(" ")
    line_count = 0
    lines = [""]
    current_line_len = 0

    for word in text_arr:
        # Skip empty words resulting from multiple spaces
        if not word:
            continue

        # Check if adding the next word exceeds the max length
        # Add 1 for the space after the word
        if current_line_len + len(word) + 1 > max_chars_per_line and current_line_len > 0:
            # Start a new line
            line_count += 1
            lines.append(word + " ")
            current_line_len = len(word) + 1
        else:
            # Add word to the current line
            lines[line_count] += word + " "
            current_line_len += len(word) + 1

    # Get rid of trailing whitespaces at the end of each line
    lines = [line.strip() for line in lines]

    # Convert list to formatted text
    formatted_text = "\n".join(lines)
    # Adjust line_count as it's 0-indexed
    actual_line_count = line_count + 1 if formatted_text else 0

    return (formatted_text, actual_line_count)

def create_text_image(text="", target_width=1080, target_height=1920, output_path="./assets/temp/quote_image.png", text_color="black", bg_color="white"):
    """Creates an image with text, scaled and wrapped based on target dimensions."""

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if not text:
        text = random_quote()

    # --- Dynamic calculations based on target dimensions ---
    # Calculate font size relative to target dimensions, taking the minimum constraint
    # Add a minimum font size (e.g., 15)
    font_size_h = int(target_height / 30) # Adjusted divisor
    font_size_w = int(target_width / 20)  # Adjusted divisor based on width
    font_size = max(15, min(font_size_h, font_size_w)) # Take minimum relative size, ensure minimum absolute size

    # Estimate max characters per line based on target width and font size
    # Add a minimum character limit (e.g., 15)
    approx_char_width = font_size * 0.6 # Adjusted factor based on typical font aspect ratio
    max_chars_per_line = max(15, int(target_width * 0.8 / approx_char_width)) if approx_char_width > 0 else 30 # Use 80% of width for text

    # Format text using the calculated max characters per line
    formatted_text, _ = text_format(text, max_chars_per_line)

    # Padding relative to font size
    pad_x = int(font_size * 1.0) # Adjusted padding
    pad_y = int(font_size * 0.6) # Adjusted padding
    # --- End dynamic calculations ---

    # Load a font, using a default fallback if not found
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # Fallback to default font if Arial is not found
        print("Arial font not found. Using default font.")
        try:
            # Try loading a known system font path as fallback
            system_fonts = [
                "C:/Windows/Fonts/arial.ttf", # Windows
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", # Linux (Debian/Ubuntu)
                "/Library/Fonts/Arial.ttf" # macOS
            ]
            font_path_found = None
            for font_path in system_fonts:
                if os.path.exists(font_path):
                    font_path_found = font_path
                    break
            if font_path_found:
                font = ImageFont.truetype(font_path_found, font_size)
            else:
                font = ImageFont.load_default() # Absolute fallback
        except Exception as e:
            print(f"Error loading system font: {e}. Using default.")
            font = ImageFont.load_default()

    # Measure text bounding box for multiline text using the chosen font
    # Use a temporary drawing context to calculate dimensions accurately
    temp_img = Image.new("RGBA", (1, 1)) # Small temp image
    temp_draw = ImageDraw.Draw(temp_img)
    try:
        # Use textbbox for modern Pillow versions
        text_bbox = temp_draw.multiline_textbbox((0, 0), formatted_text, font=font, spacing=int(font_size * 0.2))
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
    except AttributeError:
        # Fallback for older Pillow versions using textsize
        text_size = temp_draw.multiline_textsize(formatted_text, font=font, spacing=int(font_size * 0.2))
        text_width = text_size[0]
        text_height = text_size[1]

    # Determine final image dimensions based on text size and padding
    width = text_width + 2 * pad_x
    height = text_height + 2 * pad_y
    image_size = (int(width), int(height)) # Ensure integer dimensions

    # Create a new image with the specified background color
    # Handle color names and potential RGBA tuples for transparency
    try:
        img = Image.new("RGBA", image_size, color=bg_color)
    except ValueError: # Handle cases where bg_color might be invalid, default to white
        print(f"Invalid background color '{bg_color}'. Defaulting to white.")
        img = Image.new("RGBA", image_size, color="white")

    # If the desired background is not transparent, composite onto a solid background
    # This ensures text drawn on RGBA (with potential alpha) shows correctly on a solid color
    if img.mode == 'RGBA' and bg_color != (0, 0, 0, 0) and not (isinstance(bg_color, str) and bg_color.lower() == 'transparent'):
        # Create a solid background image
        background = Image.new("RGB", img.size, bg_color)
        # Paste the text image (which might have alpha) onto the solid background
        background.paste(img, (0, 0), img)
        img = background # Replace the RGBA image with the composited RGB image

    d = ImageDraw.Draw(img) # Draw on the potentially new background image

    # Calculate the position to center the text block within the image
    text_x = pad_x
    text_y = pad_y

    # Draw multiline text onto image
    try:
        d.multiline_text((text_x, text_y), formatted_text, font=font, fill=text_color, spacing=int(font_size * 0.2), align="center")
    except TypeError: # Handle older Pillow versions that might not support align
        d.multiline_text((text_x, text_y), formatted_text, font=font, fill=text_color, spacing=int(font_size * 0.2))

    img.save(output_path)
    return output_path