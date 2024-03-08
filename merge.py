from moviepy.editor import *

clip1 = VideoFileClip("myvideo.mp4").subclip(2, 10)
clip2 = VideoFileClip("myvideo2.mp4").subclip(2, 10)

clip2 = clip2.set_position((45, 150))

final_video = concatenate_videoclips([clip1, clip2])
final_video.write_videofile("FinalVideo.mp4")