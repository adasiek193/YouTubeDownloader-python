from pytube import YouTube
import subprocess

video_link = input("Paste yt link here: ")

yt = YouTube(video_link)

video = yt.streams.first()

if video is not None:
    path = video.download('Downloads')
    subprocess.Popen(f'explorer "{path}"')
else:
    print("error stupid ass bitch")

