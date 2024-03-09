from pytube import Playlist

py = Playlist("enter playlist link from youtube")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()