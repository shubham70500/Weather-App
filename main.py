from tkinter import *
from tkinter import ttk
import requests 

def getData ():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b3da361eda825535e483368360a5595b").json()
    w_label1['text']=data['weather'][0]['main']
    wd_label1['text']=data['weather'][0]['description']
    temp_label1['text']=str(data['main']['temp']-273.15)
    pre_label1['text']=data['main']['pressure']

tk = Tk()   
tk.title("Weather App")
tk.config(bg="lightblue")
tk.geometry("500x500")

name_label = Label(tk, text="Weather App", bg="lightblue" ,font=("Times 20 bold",40,"bold"))
name_label.place(x=25,y=25,height=50,width=450)

city_name = StringVar()
state_list =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(tk, width = 27,values=state_list ,font=("Times 20 bold",20),textvariable=city_name)
com.place(x=25,y=100,height=40,width=450)

w_label = Label(tk, text="Weather climate", bg="lightblue" ,font=("Times 20 bold",15))
w_label.place(x=25,y=180,height=25,width=210)
w_label1= Label(tk, text="", bg="lightblue" ,font=("Times 20 bold",15))
w_label1.place(x=250,y=180,height=25,width=210)

wd_label= Label(tk, text="Weather description", bg="lightblue" ,font=("Times 20 bold",15))
wd_label.place(x=25,y=220,height=25,width=210)
wd_label1= Label(tk, text="", bg="lightblue" ,font=("Times 20 bold",15))
wd_label1.place(x=250,y=220,height=25,width=210)

temp_label = Label(tk, text="Temperature", bg="lightblue" ,font=("Times 20 bold",15))   
temp_label.place(x=25,y=260,height=25,width=210)
temp_label1= Label(tk, text="", bg="lightblue" ,font=("Times 20 bold",15))
temp_label1.place(x=250,y=260,height=25,width=210)

pre_label= Label(tk, text="Pressure", bg="lightblue" ,font=("Times 20 bold",15))
pre_label.place(x=25,y=300,height=25,width=210)
pre_label1= Label(tk, text="", bg="lightblue" ,font=("Times 20 bold",15))
pre_label1.place(x=250,y=300,height=25,width=210)

done_button = Button(tk, text="Done", bg="lightblue" ,font=("Times 20 bold",20,"bold"),command=getData) 
done_button.place(x=200,y=350,height=50,width=100)

tk.mainloop()
