from moviepy.editor import *

# clip = VideoFileClip("myvid.mp4")
# clip.save_Frame("SS.jpg", t = 10,)
#t = 10 -> takes ss of 10 sec 


clip = VideoFileClip("myvid.mp4").subclip(0, 10)
clip = clip.margin(60)
clip.write_videofile("newvid.mp4")

