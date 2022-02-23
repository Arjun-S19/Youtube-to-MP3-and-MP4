from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
video_url = input("Enter URL: ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# print(" ") <--- ADD PATH
