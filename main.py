import yt_dlp

def download_song(song_name):
    search_url = f"ytsearch1:{song_name}"  # Searches and picks first result
    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # Output file name
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        print(f"🔍 Searching and downloading: {song_name}")
        ydl.download([search_url])
        print("✅ Download complete!")

# --- Main program ---
song = input("🎵 Enter the name of the song you want to download: ")
download_song(song)
