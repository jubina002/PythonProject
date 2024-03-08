# pip install moviepy
from moviepy.editor import *

clip_1 = VideoFileClip("demo1.mp4").subclip(00, 10)
clip_2 = VideoFileClip("demo2.mp4").subclip(00, 10)
clip_3 = VideoFileClip("demo3.mp4").subclip(00, 10)
clip_4 = VideoFileClip("demo4.mp4").subclip(00, 10)

comb = clips_array([[clip_1, clip_2], 
                   [clip_3, clip_4]])
comb.write_videofile("test.mp4")

