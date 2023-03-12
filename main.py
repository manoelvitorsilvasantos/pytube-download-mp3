from mp3Tube import Mp3Download
from mp4Tube import Mp4Download 


if __name__ == "__main__":
	try:
		param1 = argv[1]
		try:
			param2 = argv[2]
		except:
			print('./mp3Tube.py -choice <mp4/mp3> <url_youtube_video>')
			try:
				url = argv[3]
				if param2 == 'mp3':
					instance = Mp3Download(url)
					print("Downloading file mp3...")
					instance.init()
				elif param2 == 'mp4':
					instance = Mp4Download(url)
					print("Downloading file mp4")
					instance.init()
			except:
				print('./mp3Tube.py -choice <mp4/mp3> <url_youtube_video>')
	except ValueError:
		print('./mp3Tube.py -choice <mp4/mp3> <url_youtube_video>')
