from moviepy.editor import *

main_video = VideoFileClip("myvideo.mp4").subclip(2, 10)
main_video = main_video.without_audio()

main_audio = AudioFileClip("myaudio2.mp3")
final_vid = main_video.set_audio(main_audio)
final_vid.write_videofile("FinalVideo.mp4")

# step by step process 
# clip1 = VideoFileClip("myvideo.mp4").subclip(2, 10)
# clip1.audio.write_audiofile("myaudio.mp3") #turning vid to audio

# clip2 = VideoFileClip("myvideo2.mp4").subclip(3, 25)
# clip2.audio.write_audiofile("myaudio2.mp3") 

# clip1 = VideoFileClip("myvideo.mp4").subclip(2, 10)
# clip1 = clip1.without_audio()
# clip1.write_videofile("vidwithnoaudio.mp4")
# #removing audio from 'myvideo.mp4' video

# video_file = VideoFileClip("vidwithnoaudio.mp4")
# audio_file = AudioFileClip("myaudio2.mp3")

# final_vid = video_file.set_audio(audio_file)
# final_vid.write_videofile("FinalVideo.mp4")


