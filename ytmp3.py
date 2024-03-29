import yt_dlp
def run():
    video_url = input("Enter URL: ")
    video_info = yt_dlp.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    # print(" ") <--- ADD PATH

if __name__=='__main__':
    run()
