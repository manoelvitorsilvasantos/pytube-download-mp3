from pytube import YouTube
from moviepy.editor import *
from os import system

#classe para baixar música.
class MP3Download:

	def __init__ (self, url):
		self.url = url

	# make download of the file 
	def init(self):
		video = YouTube(self.url)
		audio = video.streams.filter(only_audio=True).order_by('abr').last()
		audio.download()
		clip = AudioFileClip(audio.default_filename)
		clip.write_audiofile(audio.default_filename.replace('.webm', '.mp3'))
		os.remove(audio.default_filename)




