from moviepy.editor import *
video = VideoFileClip("jk,mp4").subclip(00, 2).rotate(120)
video.write_gif("Test1.gif")