# 🎬 YT Converter

> Paste a YouTube link. Get an MP3 or MP4. That's it.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/powered%20by-yt--dlp-red)
![FFmpeg](https://img.shields.io/badge/FFmpeg-required-007808?logo=ffmpeg&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6?logo=windows&logoColor=white)

A lightweight command-line tool that downloads YouTube videos as **MP3 audio** or **full-quality MP4 video** (picture + sound merged automatically).

---

## ⚡ Demo

```text
Welcome to my YT to MP3/MP4 Converter
=====================================

Paste your link here: https://www.youtube.com/watch?v=bK5TMc71FI4
Choose your own format

        [1]MP3
        [2]MP4

Answer: 2
Formato escolhido MP4
[info] bK5TMc71FI4: Downloading 1 format(s): 400+251
[download] 100% of   40.92MiB in 00:00:08 at 4.92MiB/s
[Merger] Merging formats into "Minecraft Beaten In 28 Seconds [...].mp4"
```

## ✨ Features

- 🎵 **MP3** – extracts the best available audio and converts it to MP3
- 🎥 **MP4** – grabs the best video *and* best audio streams and merges them into one file
- 🔗 Accepts both `youtube.com/watch?v=` and short `youtu.be/` links
- 🚫 Rejects invalid links and asks again

## 📦 Requirements

| Tool | Why | Install (Windows) |
|------|-----|-------------------|
| [Python 3.10+](https://www.python.org/) | runs the program | [python.org](https://www.python.org/downloads/) |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | downloads from YouTube | `pip install yt-dlp` |
| [FFmpeg](https://ffmpeg.org/) | converts to MP3 and merges video + audio | `winget install --id Gyan.FFmpeg -e` |
| [Deno](https://deno.com/) | lets yt-dlp solve YouTube's JavaScript checks | `winget install --id DenoLand.Deno -e` |

> ⚠️ After installing FFmpeg and Deno, **restart your terminal / VS Code** so they're found.

## 🚀 Usage

```bash
git clone https://github.com/lou7523/ytconverter.git
cd ytconverter
pip install yt-dlp
python main.py
```

Paste a link, choose `1` for MP3 or `2` for MP4, and the file appears in the project folder.

## 🛠️ How it works

```text
link ──► validate ──► choose format ──► yt-dlp downloads
                                          │
                     MP3: FFmpeg extracts audio ──► .mp3
                     MP4: FFmpeg merges video + audio ──► .mp4
```

YouTube stores video and audio as **separate streams**, so the MP4 option requests both (`bv*+ba/b`) and lets FFmpeg stitch them together. Without that, you get a video with no sound (learned that the hard way 😅).

## 🗺️ Roadmap

- [x] MP3 download
- [x] MP4 download with audio
- [ ] Friendly error messages instead of tracebacks (`try` / `except`)
- [ ] Download history saved to JSON
- [ ] Stats: total downloads, hours downloaded, most used format
- [ ] Choose the output folder
- [ ] Download whole playlists

## 🧠 What I learned

- Splitting a program into functions and passing data between them with parameters
- Reading library documentation (yt-dlp) and turning it into working code
- How YouTube serves video and audio separately, and how FFmpeg merges them
- Reading Python tracebacks: last line = what broke, your file's lines = where
- Using `.gitignore` to keep large media files out of the repo

## ⚖️ Disclaimer

This project is for **educational purposes**. Only download content you own, content licensed for reuse (e.g. Creative Commons), or content you have permission to save. Respect YouTube's Terms of Service and copyright law.

---

Made by [@lou7523](https://github.com/lou7523) · Week 2 of my 50-week AI engineering roadmap 🚀
