# pip install moviepy
# pip install ez_setup
# pip install numpy
# Download image magic.exe from the link
# https://www.imagemagick.org/script/download.php#windows
# while installing click on the 'install legacy utilities(e.g. convert)'

from moviepy.editor import *
clip = VideoFileClip("demo1.mp4").subclip(00, 10)
watermark = TextClip("Hey", fontsize=50, color="plum")
watermark = watermark.set_position("center").set_duration(10)
video = CompositeVideoClip([clip, watermark])
video.write_videofile("Finalvid.mp4")