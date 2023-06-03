import json
import tkinter as tkr
import json
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
from Register_new_customer_tkinter_backend import NewClient
import time
def submition_button():
    import Register_new_customer_tkinter
    


def menuloop ():
    window = tkr.Tk();
    window.title("Barberia JLU - Menu -")
    mainFrame = tkr.Frame((window))
    mainFrame.pack();
    window.geometry("940x940")


    newclientregister = tkr.Button(mainFrame, text= "Registar nuevo cliente",command=submition_button)
    newclientregister.grid(row=0,column=0,sticky="news",padx=20,pady=20);
    window.mainloop()
menuloop()