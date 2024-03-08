from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    w_lab1.config(text=data['weather'][0]["main"])
    wd_lab1.config(text=data['weather'][0]["description"])
    temp_lab1.config(text=str(int(data['main']["temp"]-273.15)))
    per_lab1.config(text=data['main']["pressure"])
win = Tk()
win.title(" Weather")
win.geometry("500x570")
win.config(bg = "mediumpurple")


name_lab = Label(win, text="Weather App", font=('Times New Roman', 30, "bold"))
name_lab.place(x=25, y=50, height=50, width=450)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="Weather App", values=list_name,
                    font=('Times New Roman', 20, "bold"), textvariable = city_name)
com.place(x=25, y=120, height=50, width=450)

w_lab = Label(win, text="Weather Climate", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
w_lab.place(x=25, y=260, height=50, width=210)
w_lab1 = Label(win, text=" ", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
w_lab1.place(x=250, y=260, height=50, width=210)

wd_lab= Label(win, text="Weather Description", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
wd_lab.place(x=25, y=330, height=50, width=210)
wd_lab1 = Label(win, text=" ", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
wd_lab1.place(x=250, y=260, height=50, width=210)

temp_lab = Label(win, text="Temperature", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
temp_lab.place(x=25, y=400, height=50, width=210)
temp_lab1 = Label(win, text=" ", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
temp_lab1.place(x=250, y=260, height=50, width=210)

per_lab= Label(win, text="Pressure", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
per_lab.place(x=25, y=470, height=50, width=210)
per_lab1 = Label(win, text=" ", font=('Times New Roman', 15, "bold"), bg = "mediumpurple")
per_lab1.place(x=250, y=260, height=50, width=210)

button = Button(win, text="Check", font=('Times New Roman', 20, "bold"), command=data_get)
button.place(x=200, y=198, height=50, width=100)
win.mainloop()


# To get the API
# https://openweathermap.org/api
# register your account
# Go to Current & Forecast weather data collection
# Current Weather Data
# Click on API Doc based on city name, etc
# Copy the first api link
# Get API key by clicking on the link -> API key
# "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}")
