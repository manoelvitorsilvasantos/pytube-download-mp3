from pytube import*

while True:
    try:
        url = str(input('Url playlist >> '))
        p = Playlist(url)
        print(f'Downloding video by: {p.title}')
        for video in p.videos:
            video.streams.filter(only_audio=True).get_by_itag(140).download('C:\\Users\\mvictor\\Music\\metal\\All That Remains\\')
    except:
        print('Error ao baixar playlist')
