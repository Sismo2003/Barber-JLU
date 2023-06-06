import json
import tkinter as tkr
import json
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
import time

def submition_button():
    showdatawindow = tkr.Toplevel()
    showdatawindow.title("Mostrar Cliente");
    showdatawindow.geometry("600x500")
    showdataframe = tkr.Frame(showdatawindow)
    showdataframe.pack();
    
    showdatatitle = tkr.Label(showdataframe,text="Mostrar informacion sobre algun cliente: ")
    showdatatitle.grid(row=0,column=0)

    usernamelabel = tkr.Label(showdataframe,text="Ingrese el Nombre completo del cliente a buscar: ")
    usernamelabel.grid(row=1,column=2)
    userentry = tkr.Entry(showdataframe)
    userentry.grid(row=2,column=2)

    showdatawindow.mainloop()




def mainmenu():
    global window,barberimg,jluimg 
    window = tkr.Tk();
    window.title("Barberia JLU - Menu -")
    window.configure(bg='#FFFFFF')
    window.geometry("640x540")
    barberframe = tkr.Frame(window)
    barberframe.pack()

    mainFrame = tkr.Frame((window))
    mainFrame.pack();
    mainFrame.configure(bg='#FFFFFF')
    newclientregister = tkr.Button(mainFrame, text= "Registar nuevo cliente",command=submition_button)
    newclientregister.grid(row=0,column=0,sticky="news",padx=20,pady=20);

    window.mainloop()

mainmenu()