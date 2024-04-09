from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=XJouyK8geAE')

yt.streams.filter(progressive=True, file_extension="mp4",resolution="1080p").order_by('resolution').desc().first().download()

print("done")
# yt.download()

# # you = YouTube('https://www.youtube.com/watch?v=XJouyK8geAE')

# YouTube('https://www.youtube.com/watch?v=XJouyK8geAE').streams.first().download()

# # you.download()