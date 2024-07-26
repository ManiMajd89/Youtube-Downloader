import yt_dlp

def download_youtube_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path to save the video (leave blank to save in current directory): ")

    if not save_path:
        save_path = '.'

    download_youtube_video(url, save_path)
