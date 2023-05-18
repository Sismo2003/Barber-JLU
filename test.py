import json
import tkinter
import json
import time 
from tkinter import ttk

def enter_data():
    firstname1 = firstname_entry.get()
    lastname1 = lastname_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    completecourses = numberlabel_spinbox.get()
    statuscheclk = reg_status_var.get()        





    print(f"First name: {firstname1}     Last name: {lastname1}")
    print(f"Tile: {title}  age: {age}  Nationality: {nationality} ")
    print(f"Registartion status: {statuscheclk}")
    print("-----------------------------------------------------------")


window = tkinter.Tk();
window.title("JLU     --Testing--   ")
#window.geometry("800x800")

frame = tkinter.Frame(window);
frame.pack();
#saving user information




user_infoFrame = tkinter.LabelFrame(frame,text="User Information")
user_infoFrame.grid(row= 0 ,column= 0, padx=20,pady=10)

firstname = tkinter.Label(user_infoFrame,text="First name: ");
firstname.grid(row=0,column=0)
firstname_entry = tkinter.Entry(user_infoFrame)
firstname_entry.grid(row=1,column=0)


lastname= tkinter.Label(user_infoFrame,text="Lastname");
lastname.grid(row=0,column=1 )
lastname_entry = tkinter.Entry(user_infoFrame)
lastname_entry.grid(row=1,column= 1)

title_lable = tkinter.Label(user_infoFrame,text="Title")
title_combobox = ttk.Combobox(user_infoFrame,values=[" ","Mr.","Dr."])
title_lable.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label = tkinter.Label(user_infoFrame,text="age")
age_spinbox = tkinter.Spinbox(user_infoFrame,from_= 0, to=100);
age_spinbox.grid(row=3, column=0)
age_label.grid(row=2,column=0)

nationality_label = tkinter.Label(user_infoFrame,text="Nationality")
nationality_combobox = ttk.Combobox(user_infoFrame, values=["Mexico","USA","Puerto Rico"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)


for widget in user_infoFrame.winfo_children():
    widget.grid_configure(padx=10,pady=5);

#saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar()
registered_check = tkinter.Checkbutton(courses_frame,text="Currently registered",variable=reg_status_var,onvalue="Registered",offvalue="Not registered")

registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)


numberlabel = tkinter.Label(courses_frame,text="#complete courses")
numberlabel_spinbox = tkinter.Spinbox(courses_frame,from_=0,to='infinity')
numberlabel.grid(row=0,column=1)
numberlabel_spinbox.grid(row=1,column=1)




for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5);



#accept terms 
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.")
terms_check.grid(row=0,column=0)

#button

button = tkinter.Button(frame,text="Enter data", command = enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)


window.mainloop()
