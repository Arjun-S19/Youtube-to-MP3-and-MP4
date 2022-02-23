import youtube_dl
def run():
    video_url = input("Enter URL: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    print("File at -> This PC > Windows(C:) > Users > arjns > PyCharmProjects > Youtube to MP3 & MP4")

if __name__=='__main__':
    run()