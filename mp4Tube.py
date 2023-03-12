from pytube import YouTube

class MP4Download:
    def __init__ (self, url):
        self.url = url

    def getDownload(self):
        yt = YouTube(self.url)
        video = yt.streams.get_highest_resolution()
        print("Downloading...")
        out_file = video.download('./video')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        print(yt.title + "downloaded with successfully...")
        

        