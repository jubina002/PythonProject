from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MDLabel(text="Welcome to my Git", halign="center")
    if __name__ == '__main__':
        Main_App().run() #run time and again

# open chrome and type google collab
# https://colab.research.google.com/drive/1VXNf8r1jR69j3gqU5OJ4XHrYQZtiM3di
# write the following code:
# !pip install buildozer

# !pip install cython==0.29.19

# !sudo apt-get install -y
# python3-pip
# build-essential
# git
# python3
# python3-dev
# ffmpeg
# libsdl2-dev
# libsdl2-image-dev
# libsdl2-mixer-dev
# libsdl2-ttf-dev
# libportmidi-dev
# libswscale-dev
# libavformat-dev
# libavcodec-dev
# zlib1g-dev

# !sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev 
#libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6

# !sudo apt-get install libffi-dev

# (import main.py in googlecollab -> file)
# !buildozer init
# (Note: 
# press y
# open buildozer.spec
# in 39 line add-> ==2.0.0, kivymd, pillow
# your line will look like this -> requirements = python3,kivy==2.0.0, kivymd, pillow)

# !buildozer -v android debug
# (press y
# 'bin' folder is created in the googlecollab file
# download the file under it
# From your pc's downloads send it to your phone to check the app)