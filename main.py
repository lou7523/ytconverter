from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

def main():
    print("Welcome to my YT to MP3/MP4 Converter\n\n"
          "=====================================\n\n\n")

    textgood = False
    while textgood == False:
        text = input("Paste your link here: ")
        if text.startswith("https://www.youtube.com/watch?v=") or text.startswith("https://youtu.be/") or text.startswith("https://youtube.com") or text.startswith("https://m.youtube.com") or text.startswith("https://www.youtube.com/shorts/"):
            format(text)
            textgood = True
        else:
            print("Error! Invalid Link...")
            textgood = False

def format(text):
    formatvalid = False
    while not formatvalid:
        chooseformat = input("Choose your own format\n\n\t[1]MP3\n\t[2]MP4\n\nAnswer: ")
        if chooseformat == '1':
            print("Format MP3")
        
            ydl_opts = {
                'format': 'mp3/bestaudio/best',
                'postprocessors': [{    
                    'key':  'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]
            }
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([text])
            except DownloadError:
                print("Error when downloading...")
            formatvalid = True
        elif chooseformat == '2':
            print("Format MP4")
    
            ydl_opts = {
            'format': 'bv*+ba/b',
            'merge_output_format': 'mp4'
        }

            try:
                with YoutubeDL(ydl_opts) as ydl:
                    error_code = ydl.download([text])
            except DownloadError:
                print("Error when downloading...")
            formatvalid == True
        else:
            print("Error! Choose an existing format...")
            formatvalid = False

if __name__ == '__main__':
    main()