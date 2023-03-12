
#!/usr/bin/python

from pytube import YouTube
from moviepy.editor import *
from sys import argv
from os import system

#classe para baixar música.
class MP3Download:

	def __init__ (self, url):
		self.url = url

	def init(self):
		video = YouTube(self.url)
		audio = video.streams.filter(only_audio=True).order_by('abr').last()
		audio.download()
		clip = AudioFileClip(audio.default_filename)
		clip.write_audiofile(audio.default_filename.replace('.webm', '.mp3'))
		os.remove(audio.default_filename)


if __name__ == "__main__":
	try:
		url = argv[1]
		instance = MP3Download(url)
		print("Downloading file...")
		instance.init()
	except ValueError:
		print('./mp3Tube.py <url_youtube_video>')



