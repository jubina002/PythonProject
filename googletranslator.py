from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="Type", src="English", dest = "Spanish"):
    text1 = text
    src1 = src
    dest1 =dest
    trans= Translator()
    trans1 = trans.translate(text, src = src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text = msg, src = s, dest = d)
    dest_txt.delete(1.0, END)


root = Tk()
root.title(" Translator")
root.geometry("500x700")
root.config(bg="Greenyellow")

lab_txt = Label(root, text="Translator", font=("Times New Roman", 35, "bold"),
               bg="Greenyellow", fg="black")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side = BOTTOM) 
# pack(): organizes widgets in horizontal and vertical boxes 
# that are limited to left, right, top, bottom positions offset and relative to each other within a frame
lab_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"),
               bg="Hotpink", fg="black")
lab_txt.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap = WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, value = list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("--Choose one--")
button_change = Button(frame, text = "Translate", relief= RAISED, command = data)
button_change.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(frame, value = list_text)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("--Choose one--")

lab_txt = Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"),
               bg="Hotpink", fg="black")
lab_txt.place(x=100, y=360, height=20, width=300)
dest_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap = WORD)
dest_txt.place(x=10, y=400, height=150, width=480)




root.mainloop()