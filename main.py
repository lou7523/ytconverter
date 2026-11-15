from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

liststarts = [
    "https://www.youtube.com/watch?v=",
    "https://youtu.be/",
    "https://youtube.com",
    "https://m.youtube.com",
    "https://www.youtube.com/shorts/",
]

def main():
    print("Welcome to my YT to MP3/MP4 Converter\n\n"
          "=====================================\n\n\n")
    
    textgood = False
    downloadAgain = True
    while downloadAgain == True:
        while textgood == False:
            text = input("Paste your link here: ")
            for x in liststarts:
                if text.startswith(x):
                    choose_format(text)
                    textgood = True
                    break
            else:
                print("ERROR! Invalid Link...")   
        answerDownload = input("Would you like to download another file (y/n): ")
        if answerDownload.lower == 'y':
            downloadAgain = True
            textgood = False
        elif answerDownload.lower == 'n':
            print("Closing...")
            downloadAgain = False
            return
        else:
            print("Please choose (y/n)")

def choose_format(text):
    formatvalid = False
    try:
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

                formatvalid = True
            elif chooseformat == '2':
                print("Format MP4")
    
                ydl_opts = {
                    'format': 'bv*+ba/b',
                    'merge_output_format': 'mp4'
                }

                formatvalid = True
            else:
                print("Error! Choose an existing format...")
                formatvalid = False

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([text])
    except DownloadError:
        print("Error! Download Failed")

if __name__ == '__main__':
    main()