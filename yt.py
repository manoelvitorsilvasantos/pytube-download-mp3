from pytube import*
from sys import*
from os import chdir, getcwd, listdir
from os import *
import re

titulo = ''

def downloadMP3(path, url):
    yt = YouTube(url)
    global titulo
    titulo = yt.title
    yt.streams.filter(only_audio=True, file_extension='mp4')
    stream = yt.stream = yt.streams.get_by_itag(140)
    stream.download(path)
    chdir(path)
    getcwd()
    for file in listdir():
        output = file
        new_file = re.sub("mp4", "mp3", output)
        replace(file, new_file)
    #
def downloadMP4(path, url):
    yt = YouTube(url)
    global titulo
    titulo = yt.title
    yt.streams.get_highest_resolution().download(path)


def main():
    opc = int(input('[1] Audio - [2] Video >> '))
    if opc == 1:
        url = input('Youtube Url video >> ')
        path = input('Caminho do Arquivo >> ')
        texto = downloadMP3(path, url)
        print('{} foi baixado com sucesso...'.format(titulo))
        print('==============================================================')
    elif opc == 2:
        texto = downloadMP4(path, url)
        print('{} foi baixado com sucesso...'.format(titulo))
        print('==============================================================')
    else:
        print('Inválido')

while True:
    main()
        
    
