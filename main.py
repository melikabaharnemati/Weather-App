from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city = textfield.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YourAPIKeys"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "Feels", "Like", temp, "°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

        now = datetime.now()
        formatted_date = now.strftime("%a, %b %d, %Y")
        datetext.config(text=formatted_date)

    except Exception as e:
        messagebox.showerror("Weather App", "کشور وارد شده معتبر نمی‌باشد.")

#search box
Search_text = Label(text="Enter City: ", font=("arial", 16), fg="black")
Search_text.place(x=100, y=45)

Search_image = PhotoImage(file="images/search.png")
myimage = Label(image=Search_image)
myimage.place(x=200,y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=230, y=40)
textfield.focus()

Search_icon = PhotoImage(file="images/search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather)
myimage_icon.place(x=580, y=34)

#logo
Logo_image = PhotoImage(file="images/weather-logo.png")
logo = Label(image=Logo_image)
logo.place(x=120, y=115)

#Bottom-box
Frame_image = PhotoImage(file="images/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#date
datetext = Label(root, font=("arial", 12))
datetext.place(x=400, y=290)

#label
label1= Label(root, text="Wind", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=410)

label2= Label(root, text="Humidity", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=240, y=410)

label3= Label(root, text="Description", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=410)

label4= Label(root, text="Pressure", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=410)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 16), bg="#1ab5ef")
w.place(x=125, y=435)
h = Label(text="...", font=("arial", 16), bg="#1ab5ef")
h.place(x=250, y=435)
d = Label(text="...", font=("arial", 16), bg="#1ab5ef")
d.place(x=430, y=435)
p = Label(text="...", font=("arial", 16), bg="#1ab5ef")
p.place(x=670, y=435)

root.mainloop()