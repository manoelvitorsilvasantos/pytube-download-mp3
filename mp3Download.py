# importing packages
from pytube import YouTube
import os
  
while True:
    try:
        # url input from user
        yt = YouTube(
            str(input("Enter the URL of the video you want to download: \n>> ")))
          
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
          
        # check for destination to save file
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'
        #destination = str("C:\\Users\\mvictor\\Music\\musicas") 
        # download the file
        out_file = video.download(output_path=destination)

        print("Downloading...")
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
          
        # result of success
        print(yt.title + " has been successfully downloaded.")
    except ValueError:
        print("Houve um error!")
