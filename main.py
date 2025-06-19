import os
import yt_dlp

# Easy-to-edit paths
FFMPEG_PATH = 'C:\\Users\\vihan\\Downloads\\ffmpeg-7.1.1-essentials_build\\bin'  # Change to your FFmpeg path
DOWNLOAD_DIR = 'D:/Songs'  # Change to your download directory
SONGS_FILE = 'songs.txt'  # Name of your song list file

# Add FFmpeg to system PATH
os.environ['PATH'] += f';{FFMPEG_PATH}'

def download_song(song_name):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    search_url = f"ytsearch1:{song_name}"

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'ffmpeg_location': os.path.join(FFMPEG_PATH, 'ffmpeg.exe'),
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'extractor_args': {
            'youtube': ['client=web']
        },
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🔍 Searching and downloading: {song_name}")
            ydl.download([search_url])
            print("✅ Download complete!\n")
    except Exception as e:
        print(f"❌ Failed to download '{song_name}': {e}\n")

def download_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        songs = [line.strip() for line in f if line.strip()]

    if not songs:
        print("❌ No songs found in the file.")
        return

    print(f"📃 Found {len(songs)} songs. Starting download...\n")

    for i, song in enumerate(songs, 1):
        print(f"🎵 ({i}/{len(songs)}) {song}")
        download_song(song)

if __name__ == "__main__":
    download_from_file(SONGS_FILE)
