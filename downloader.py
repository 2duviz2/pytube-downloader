import subprocess
import sys

print("Installing modules...")

subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])

import argparse
from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "./audio"

def download(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_SAVE_DIRECTORY)
    except:
        print("Failed to download video")

    print("video was downloaded successfully")

def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download(AUDIO_SAVE_DIRECTORY)
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")


print("\n")
print("Pytube downloader (by Duviz2)")

while True:
    print("\n")
    download(input("Insert a video url: "))
