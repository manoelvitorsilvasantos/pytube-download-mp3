#!/usr/bin/env python
from mp3Tube import MP3Download
from mp4Tube import MP4Download
from sys import argv
from os import *

if __name__ == "__main__":
	try:
		opc = str(argv[1])
		url = str(argv[2])
		print(opc, url)
		if opc == "-audio":
			instance = MP3Download(url)
			print("Downloading file mp3...")
			instance.init()
		elif opc == '-video':
			instance = MP4Download(url)
			print("Downloading file mp4")
			instance.getDownload()
	except ValueError:
		print('./main.py -audio <url_youtube_video> - download mp3')
		print('./main.py -video <url_youtube_video> - download mp4')

