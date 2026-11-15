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
    donwloadAgain = True
    while donwloadAgain == True:
        while textgood == False:
            text = input("Paste your link here: ")
            for x in liststarts:
                if text.startswith(x):
                    format(text)
                    textgood = True
                    break
            else:
                print("ERROR! Invalid Link...")   
        answerDownload = input("Would you like to download another file (y/n)")
        if answerDownload == 'y' or answerDownload == 'Y':
            donwloadAgain = True
            textgood = False
        elif answerDownload == 'n' or answerDownload == 'N':
            print("Closing...")
            donwloadAgain = False
            return
        else:
            print("Please choose (y/n)")

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
            formatvalid = True
        else:
            print("Error! Choose an existing format...")
            formatvalid = False

if __name__ == '__main__':
    main()