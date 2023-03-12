from pytube import YouTube
import os

while True:
    try:
        youtube = YouTube(str(input("Digite url do video >> ")))
        destino = str(input("Digite o destino do video >> ")) or '.'
        video = youtube.streams.get_highest_resolution()
        
        print("Downloading....")
        out_file = video.download(output_path=destino)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        print(youtube.title + " baixado com sucesso.")
    except ValueError:
        print("Error")
