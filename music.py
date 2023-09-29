import os
import subprocess
import yt_dlp
from PIL import Image
import cv2

def sanitize_input(input_str):
    # Remove leading and trailing spaces and quotes
    return input_str.strip(' \'"')

def download_song(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloaded_audio.mp3',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def resize_image(image_path, output_path, target_width=1920, target_height=1080):
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Get the current dimensions of the image
    current_height, current_width, _ = img.shape

    # Calculate the scaling factors for width and height
    scale_x = target_width / current_width
    scale_y = target_height / current_height

    # Resize the image using cubic interpolation for quality
    resized_img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_CUBIC)

    # Save the resized image
    cv2.imwrite(output_path, resized_img)

def convert_audio_to_video(audio_file, image_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', audio_file,
        '-loop', '1',
        '-framerate', '2',
        '-i', image_file,
        '-c:v', 'libx264',
        '-tune', 'stillimage',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-pix_fmt', 'yuv420p',
        '-shortest',
        '-y',
        output_file,
    ]

    subprocess.run(ffmpeg_cmd)

def main():
    link = input("Enter the YouTube link of the song: ")
    image_file_input = input("Enter the path to the image file (e.g., thumbnail.jpg): ")

    # Sanitize the image file input to remove commas and quotes
    image_file = sanitize_input(image_file_input)

    if os.path.exists('downloaded_audio.mp3'):
        os.remove('downloaded_audio.mp3')

    download_song(link)

    if not os.path.exists('downloaded_audio.mp3'):
        print("Failed to download the audio.")
        return

    resized_image_file = 'resized_thumbnail.jpg'
    resize_image(image_file, resized_image_file, target_width=1920, target_height=1080)

    output_file = 'output_video.mp4'

    convert_audio_to_video('downloaded_audio.mp3', resized_image_file, output_file)

    print(f"Video with thumbnail '{resized_image_file}' created: {output_file}")

if __name__ == "__main__":
    main()
