import json
import tkinter as tkr
import json
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
import time


def load_data (treeview,toppinglist):
    try:
        with open("database.json", "r") as file:
            main = json.load(file)
        JsonList = main;
    except:
        print("error al cargar la base de datos")
    list_value = [list(JsonList.values()) for JsonList in JsonList]
    for col_names in toppinglist:
        treeview.heading(col_names,text=col_names)

    for value_tuple in list_value[0:]:
        treeview.insert('',tkr.END,values=value_tuple)






def submition_button():
    showdatawindow = tkr.Toplevel()
    showdatawindow.title("Mostrar Cliente");
   # showdatawindow.geometry("600x500")

    frame = tkr.Frame(showdatawindow)
    frame.pack();
    
    lookupframe = ttk.LabelFrame(frame, text="Busqueda del cliente")  
    lookupframe.grid(row=0,column=0,padx=20,pady=20)

    name_entry = ttk.Entry(lookupframe)
    name_entry.insert(0,"Nombre Del Cliente")
    name_entry.bind("<FocusIn>", lambda e:name_entry.delete(0,"end"))
    name_entry.grid(row=0,column=0,sticky="ew",padx=20,pady=20)

    phonenumber_entry = ttk.Entry(lookupframe)
    phonenumber_entry.insert(0,"Numero De Telefono")
    phonenumber_entry.bind("<FocusIn>",lambda e:phonenumber_entry.delete(0,"end"))
    phonenumber_entry.grid(row=1,column=0,padx=20,pady=20,sticky="ew")

    email_entry = ttk.Entry(lookupframe)
    email_entry.insert(0,"Email")
    email_entry.bind("<FocusIn>",lambda e:email_entry.delete(0,"end"))
    email_entry.grid(row=2,column=0,padx=20,pady=20,sticky="ew")

    button_entry = ttk.Button(lookupframe,text="Buscar")
    button_entry.grid(row=3,column=0,padx=20,pady=20,sticky="nsew")

    colms = ("Nombre","Fecha de Nacimiento","Telefono","Email","Barber","Corte","Frecuencia de corte","Productos","Servicios alternos","Observaciones","Visitas")

    treeframe = ttk.Frame(frame)
    treeframe.grid(row=0,column=1,pady=10)

    treescroll_y =ttk.Scrollbar(treeframe)
    treescroll_y.pack(side="right",fill="y")
    treeview_y = ttk.Treeview(treeframe,show="headings",yscrollcommand=treescroll_y.set,columns=colms,height=12)
    treescroll_y.config(command=treeview_y.yview)
    treeview_y.pack()
   
    treeview_y.column("Nombre",width=90)
    treeview_y.column("Fecha de Nacimiento",width=90)
    treeview_y.column("Telefono",width=80)
    treeview_y.column("Email",width=140)
    treeview_y.column("Barber",width=110)
    treeview_y.column("Corte",width=100)
    treeview_y.column("Frecuencia de corte",width=100)
    treeview_y.column("Productos",width=140)
    treeview_y.column("Servicios alternos",width=100)
    treeview_y.column("Observaciones",width=200)
    treeview_y.column("Visitas",width=120)
    load_data(treeview_y,colms)
    

    #treescroll_x = ttk.Scrollbar(treeframe)
    #treescroll_x.pack(side="bottom",fill="x")
    #treeview_x = ttk.Treeview(treeframe,show="headings",columns=colms,height=12)
    #treescroll_x.config(command=treeview_x.xview)
    #treeview_x.pack()
    showdatawindow.mainloop()




def mainmenu():
    global window,barberimg,jluimg 
    window = tkr.Tk();
    style = ttk.Style(window)
    window.tk.call("source","forest-dark.tcl")
    style.theme_use("forest-dark")

    window.title("Barberia JLU - Menu -")

    window.geometry("640x540")
    barberframe = tkr.Frame(window)
    barberframe.pack()

    mainFrame = tkr.Frame((window))
    mainFrame.pack();

    newclientregister = tkr.Button(mainFrame, text= "Registar nuevo cliente",command=submition_button)
    newclientregister.grid(row=0,column=0,sticky="news",padx=20,pady=20);

    window.mainloop()

mainmenu()