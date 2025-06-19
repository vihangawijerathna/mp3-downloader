import os
import yt_dlp

# ✅ Easy-to-edit paths
FFMPEG_PATH = 'C:\\Users\\vihan\\Downloads\\ffmpeg-7.1.1-essentials_build\\bin'   #Change this to your FFmpeg path
DOWNLOAD_DIR = 'D:/Songs'  # Change this to your desired download directory

# Add FFmpeg to system PATH
os.environ['PATH'] += f';{FFMPEG_PATH}'

def download_song(song_name):
    # Create download directory if it doesn't exist
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    search_url = f"ytsearch1:{song_name}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': os.path.join(FFMPEG_PATH, 'ffmpeg.exe'),
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"🔍 Searching and downloading: {song_name}")
        ydl.download([search_url])
        print("✅ Download complete!")

# Main program
song = input("🎵 Enter the name of the song you want to download: ")
download_song(song)
