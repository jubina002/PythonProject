import tkinter as tk
from tkinter import messagebox

def find_sum():
    num1 = entry1.get()
    num2 = entry2.get()
    if num1.isdigit() and num2.isdigit():
        result = float(num1) + float(num2)
        # messagebox.showinfo("Result", f"Sum: {result}")
        result_label.config(text=f"Sum: {result}")
    else:
        # messagebox.showerror("Error! Enter valid numbers")
        result_label.config(text="Error! Enter valid numbers")
    
    
    
root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

#Input field
label1 = tk.Label(root, text="Enter First number")
entry1= tk.Entry(root)
label1.pack(pady=10)
entry1.pack(pady = 5)

label2 = tk.Label(root, text="Enter Second number")
entry2= tk.Entry(root)
label2.pack(pady=10)
entry2.pack(pady = 5)

button = tk.Button(root, text="Add", command=find_sum)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()