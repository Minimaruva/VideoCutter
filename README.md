# EasyReel Quote Content Generator

A GUI built with Tkinter to easily create images or videos featuring text overlays, typically quotes, on top of user-provided background images or videos.

## Features

*   **GUI Interface:** Simple interface (`videocutter_app.py`) for selecting files, entering text, and choosing output options.
*   **Random Quote Generation:** Fetches random quotes from a CSV file (`./assets/Quotes.csv`) credits to:
*   **Text Formatting:** Automatically wraps text to fit within calculated line limits.
*   **Dynamic Text Image Creation:**
    *   Generates a text image (quote box) with specified text or a random quote.
    *   Scales font size and text wrapping based on the target background image/video dimensions.
    *   Allows customization of text color and background color for the quote box.
    *   Centers text within the quote box.
*   **Output Modes:**
    *   **Image-to-Image:** Overlays the quote box onto a background image and saves the result as a single image.
    *   **Image-to-Video:** Creates a video of a specified duration using the background image and the overlaid quote box.
    *   **Video-to-Video:** Overlays the quote box onto an existing video (optionally trimming the video duration).

## How to Use

1.  Run the application: `python videocutter_app.py`
2.  **Enter Quote:** Type your desired quote into the text box, or click "Random quote" to fetch one.
3.  **Import File:** Click "Import file" and select your background image (.png, .jpg, etc.) or video (.mp4).
4.  **(Optional) Duration:** If creating a video (img-to-video or video-to-video), enter the desired duration in seconds. Defaults to 10 seconds for img-to-video, or the full video length for video-to-video if left blank.
5.  **Select Mode:** Choose one of the radio buttons:
    *   `img-to-img`: Combine quote and background image into a new image.
    *   `img-to-video`: Create a video from the quote and background image.
    *   `video-to-video`: Overlay the quote onto the background video.
6.  **(Optional) Output Folder:** Click "Choose output folder" to select where the final file will be saved. Defaults to `./output`.
7.  **Submit:** Click "Submit for edit". The application will process the file and save it to the specified output folder. A success message will appear upon completion.

## Dependencies

*   Pillow (`PIL`)
*   Pandas
*   MoviePy

Install them using pip:
`pip install Pillow pandas moviepy`

*Note: MoviePy might require `ffmpeg` to be installed on your system.*
