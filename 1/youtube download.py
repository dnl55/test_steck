import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=jyzdSXC-2m8')
yt.filename
yt.get_videos()
videos = yt.get_videos()
for v in videos: 
    print(v)

