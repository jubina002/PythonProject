# pip install PyAutoGUI

import pyautogui
from tkinter import *

def take_ss():
    add_data = entry.get()
    path = add_data + "\\test12.png"
    ss = pyautogui.screenshot()
    ss.save(path)

win = Tk()
win.title(" ScreenShot")
win.geometry("500x500")
win.config(bg = "darkseagreen")
win.resizable(False, False)

entry = Entry(win, font=('Times New Roman', 20, "bold"))
entry.place(x=20, y=50, height=70, width=660)
button = Button(win, text="SS", font=('Times New Roman', 50, "bold"), command=take_ss)
button.place(x=250, y=140, height=100, width=200)

win.mainloop()

# To convert it into .exe File
# Go to the ScreenShot.py bhayeko folder
# open cmd -> pyinstaller --onefile ScreenShot.py
# OR
# pyinstaller -F -w -i watermelon.ico ScreenShot.py
# -F   (all in 1 file)
# -w   (removes terminal window)
# -i icon.ico  (adds custom icon to .exe)
# ScreenShot.py  (name of your main python file)
# Look inside the dist file
