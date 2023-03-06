from __future__ import unicode_literals
import yt_dlp

ydl_opts = {}
video_url = input("Enter URL: ")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# print(" ") <--- ADD PATH
