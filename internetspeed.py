# pip install tk
# pip install speedtest

from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+ "Mbps"
    up = str(round(sp.upload()/(10**6),3))+ "Mbps"
    lab_down.config(text = down)
    lab_up.config(text = up)

sp = Tk()
sp.title(" Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="Pink")


lab = Label(sp, text = "Internet Speed Test", font=("Times New Roman", 25, "bold"),
            fg="black")
lab.place(x=60, y=40, height=50, width=380)

lab= Label(sp, text = "Downloading Speed", font=("Times New Roman", 25, "bold"),
            fg="black")
lab.place(x=60, y=130, height=50, width=380)
lab_down = Label(sp, text = "00", font=("Times New Roman", 25, "bold"),
            fg="black")
lab_down.place(x=60, y=200, height=50, width=380)

lab= Label(sp, text = "Uploading Speed", font=("Times New Roman", 25, "bold"),
            fg="black")
lab.place(x=60, y=290, height=50, width=380)
lab_up = Label(sp, text = "00", font=("Times New Roman", 25, "bold"),
            fg="black")
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=("Times New Roman", 25, "bold"), relief = RAISED, bg="Skyblue",
                command= speedCheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()