from pytube import YouTube

link = "https://youtu.be/Zah4MfwTSg4"
youtube_1 = YouTube(link)

#print(youtube_1.title) //video title
#print(youtube_1.thumbnail_url) //video thumbnail

videos = youtube_1.streams.all() #download video
#audio = youtube_1.streams.filter(only_audio=True) #audio download only
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("enter : "))
videos[strm].download()
print('Successfully')    
