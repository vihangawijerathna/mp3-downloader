# MP3 Downloader

A simple Python script to search and download songs from YouTube as MP3 files using **yt-dlp** and **FFmpeg**.

## Features

* Search for songs by name on YouTube
* Automatically download the best audio available
* Convert audio to MP3 format (192 kbps)
* Save downloaded songs to a custom folder (e.g., a USB drive)
* Uses FFmpeg for audio conversion

## Requirements

* Python 3.7 or above
* yt-dlp Python package
* FFmpeg (Windows build recommended)

## Installation

1. **Install Python 3**  
   Download and install Python from [python.org](https://python.org).

2. **Install yt-dlp**  
   Open terminal or PowerShell and run:
   ```bash
   pip install yt-dlp
   ```

3. **Download FFmpeg**  
   Download a Windows build from [gyan.dev FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/)  
   Extract the zip and note the path to the `bin` folder containing `ffmpeg.exe`.

4. **Configure the script**
   * Open `main.py`
   * Set `FFMPEG_PATH` variable to your FFmpeg `bin` folder path
   * Set `DOWNLOAD_DIR` variable to your desired download folder (e.g., a USB drive path)

## Usage

Run the script from terminal or PowerShell:

```bash
python main.py
```

Enter the name of the song when prompted:

```
🎵 Enter the name of the song you want to download: shape of you
```

The script will download and convert the song, saving it as an MP3 in the specified folder.

## Example

```
🎵 Enter the name of the song you want to download: shape of you
🔍 Searching and downloading: shape of you
✅ Download complete!
```

## Troubleshooting

* **ffmpeg not found error:** Make sure `FFMPEG_PATH` points to the folder containing `ffmpeg.exe`. Also, ensure that folder is added to your system `PATH` environment variable or appended in the script as shown.
* **Permission errors:** Check you have write permission to the `DOWNLOAD_DIR`.

## License

This project is open source under the MIT License.

## Acknowledgements

* [yt-dlp](https://github.com/yt-dlp/yt-dlp) — YouTube downloader library
* [FFmpeg](https://ffmpeg.org/) — Audio/video conversion tool
* FFmpeg builds from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)