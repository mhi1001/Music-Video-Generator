# Music Video Generator

This Python script allows you to create music videos by combining an audio track from a YouTube/Soundcloud link with an image. The output video will be in MP4 format, with the image upscaled to 1920x1080 resolution.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

    Python (version 3.x recommended)
    yt-dlp (YouTube downloader)
    Pillow (Python Imaging Library)
    opencv-python (OpenCV for image processing)
    ffmpeg (for video creation)

You can install the required Python packages using the following commands:

```bash
pip install yt-dlp pillow opencv-python-headless
```

Make sure you have ffmpeg installed and added to your system's PATH. You can download it from the official website.

## How to Run

Clone or download this repository to your local machine.
Open a terminal or command prompt and navigate to the directory where the script is located.
Run the script by entering the following command:

```bash
python music.py
```

### Follow the prompts
    Enter the YouTube link of the song you want to use.
    Provide the path to an image file (e.g., thumbnail.jpg) that will be used as the video background.

The script will download the audio from the YouTube/Soundcloud link, upscale the image to 1920x1080 resolution, and create a video using the audio and image.

Expected Output

After running the script, you will find the generated music video in the same directory as the script, named as output_video.mp4.
