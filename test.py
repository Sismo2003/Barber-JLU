import json
import tkinter as tkr
import json
import datetime
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import time



def endcode ():
    exit();


def load_data (treeview,toppinglist):
    try:
        with open("config.json","r") as file:
           path = json.load(file);
    except:
        print("Error al cargar el config.json")
    try:
        with open(path.get("DatabasePath"), "r") as file:
            main = json.load(file)
        JsonList = main;
        list_value = [list(JsonList.values()) for JsonList in JsonList]
        for col_names in toppinglist:
            treeview.heading(col_names,text=col_names)

        for value_tuple in list_value[0:]:
            treeview.insert('',tkr.END,values=value_tuple)
    except:
        print("Error al cargar la base de datos.")
        return True
       #messagebox.showerror("Error en la Base de datos","Hubo un error al cargar la base de datos, verifique que el path sea el correcto.")
        



def lookupclient_button():
    showdatawindow = tkr.Toplevel()
    showdatawindow.title("Mostrar Cliente");
    #showdatawindow.geometry("1080x480")

    frame = ttk.Frame(showdatawindow)
    frame.pack();
    
    lookupframe = ttk.LabelFrame(frame, text="Busqueda del cliente")  
    lookupframe.grid(row=0,column=0,padx=20,pady=20)

    name_label = ttk.Label(lookupframe,text="Nombre del Cliente")
    name_label.grid(row=0,column=0)
    name_entry = ttk.Entry(lookupframe)
    name_entry.insert(0,"Cristiano Gomes")
    name_entry.bind("<FocusIn>", lambda e:name_entry.delete(0,"end"))
    name_entry.bind("<FocusOut>",lambda e:name_entry.insert(0,"Cristiano Gomes"))
    name_entry.grid(row=1,column=0,sticky="ew",padx=20,pady=20)


    phonenumber_label = ttk.Label(lookupframe,text="Numero Telefonico")
    phonenumber_label.grid(row=2,column=0)
    phonenumber_entry = ttk.Entry(lookupframe)
    phonenumber_entry.insert(0,"+52 33 1234 5678")
    phonenumber_entry.bind("<FocusIn>",lambda e:phonenumber_entry.delete(0,"end"))
    phonenumber_entry.bind("<FocusOut>",lambda e:phonenumber_entry.insert(0,"+52 33 1234 5678"))
    phonenumber_entry.grid(row=3,column=0,padx=20,pady=20,sticky="ew")



    email_label = ttk.Label(lookupframe,text="Correo Electronico")
    email_label.grid(row=4,column=0)
    email_entry = ttk.Entry(lookupframe)
    email_entry.insert(0,"example@dominio.com")
    email_entry.bind("<FocusIn>",lambda e:email_entry.delete(0,"end"))
    email_entry.bind("<FocusOut>",lambda e:email_entry.insert(0,"example@dominio.com"))
    email_entry.grid(row=5,column=0,padx=10,pady=10,sticky="ew")

    button_entry = ttk.Button(lookupframe,text="Buscar")
    button_entry.grid(row=6,column=0,sticky="nsew",padx=20,pady=20)

    returntomenu_button = ttk.Button(lookupframe,text="Regresar al menu",command=endcode)
    returntomenu_button.grid(row=7,column=0,padx=20,pady=20,sticky="nsew")

    colms = ("Nombre","Fecha de Nacimiento","Telefono","Email","Barber","Corte","Frecuencia de corte","Productos","Servicios alternos","Observaciones","Visitas")


    treeframe = ttk.Frame(frame)
    treeframe.grid(row=0, column=1, pady=20,sticky="news",padx=20)
    treeframe.columnconfigure(0,weight=1)
    treeframe.rowconfigure(0,weight=1)
    treeframe.rowconfigure(1,weight=1)

    treeview = ttk.Treeview(treeframe, show="headings", columns=colms)
    
    treeview.column("Nombre",width=30)
    treeview.column("Fecha de Nacimiento",width=30)
    treeview.column("Telefono",width=30)
    treeview.column("Email",width=30)
    treeview.column("Barber",width=30)
    treeview.column("Corte",width=30)
    treeview.column("Frecuencia de corte",width=30)
    treeview.column("Productos",width=30)
    treeview.column("Servicios alternos",width=30)
    treeview.column("Observaciones",width=30)
    treeview.column("Visitas",width=30)
   

    scrollbar_y = ttk.Scrollbar(treeframe,orient='vertical',command=treeview.yview)
    scrollbar.grid(row=1,column=0,sticky="new")
    
    treeview.configure(xscroll=scrollbar.set)
    treeview.grid(row=0, column=0, sticky="nsew")

    #treeview_y.pack(side="left", fill="both", expand=True)
    





    load_data(treeview,colms)
    
    #treescroll_y =ttk.Scrollbar(treeframe)
    #treescroll_y.pack(side="right",fill="y")
    #treeview_y = ttk.Treeview(treeframe,show="headings",yscrollcommand=treescroll_y.set,columns=colms,height=12)
    #treescroll_y.config(command=treeview_y.yview)
    #treeview_y.pack()
    #treeview_y.configure(xscrollcommand=Scrollbar.set)
    
    
    #treescroll_x = ttk.Scrollbar(treeframe)
    #treescroll_x.pack(side="bottom",fill="x")
    #treeview_x = ttk.Treeview(treeframe,show="headings",columns=colms,height=12)
    #treescroll_x.config(command=treeview_x.xview)
   
    
  
    showdatawindow.protocol("WM_DELETE_WINDOW",endcode)
    showdatawindow.mainloop()


lookupclient_button()