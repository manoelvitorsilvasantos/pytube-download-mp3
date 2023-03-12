from pytube import YouTube

class Mp4Download:
	
	def __init__(self, url):
		self.url = url

	def init(self):
		outube = YouTube(self.url)
        video = youtube.streams.get_highest_resolution()
        print("Downloading....")
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        print(youtube.title + " baixado com sucesso.")
