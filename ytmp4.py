from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
video_url = input("Enter URL: ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("File at -> This PC > Windows(C:) > Users > arjns > PyCharmProjects > Youtube to MP3 & MP4")
