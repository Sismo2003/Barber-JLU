import json
import tkinter as tkr
import json
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
import time
from Register_new_customer_backend import *

with open("hair_products.json", "r") as file:
    hair_products_list = json.load(file)

with open("alternave_services.json", "r") as file:
    alternave_services_json = json.load(file)
    
 
def ebf ():
    messagebox.showwarning("Cierre de programa","Estas apunto de cerrar el programa, estas actualmente ingresando los datos de un cliente.")
    exit();
    
def endcode ():
    exit();

def returntomenu (winclose):
    winclose.destroy()
    window.deiconify()

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


def lookupclient_button():
    showdatawindow = tkr.Toplevel()
    showdatawindow.title("Mostrar Cliente");
   # showdatawindow.geometry("600x500")

    frame = ttk.Frame(showdatawindow)
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

    returntomenu_button = ttk.Button(lookupframe,text="Regresar al menu",command=lambda: returntomenu(showdatawindow))
    returntomenu_button.grid(row=4,column=0,padx=20,pady=20,sticky="nsew")

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
    treeview_y.column("Email",width=120)
    treeview_y.column("Barber",width=100)
    treeview_y.column("Corte",width=100)
    treeview_y.column("Frecuencia de corte",width=100)
    treeview_y.column("Productos",width=120)
    treeview_y.column("Servicios alternos",width=100)
    treeview_y.column("Observaciones",width=180)
    treeview_y.column("Visitas",width=120)
    load_data(treeview_y,colms)
    

    #treescroll_x = ttk.Scrollbar(treeframe)
    #treescroll_x.pack(side="bottom",fill="x")
    #treeview_x = ttk.Treeview(treeframe,show="headings",columns=colms,height=12)
    #treescroll_x.config(command=treeview_x.xview)
    #treeview_x.pack()
    showdatawindow.mainloop()



def theme_mode (interruptor,style):
    if interruptor.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

def submition_button(window):
    window.withdraw()
    NewClient()

def NewClient():
    def submtion_data ():
        firstName = first_name_entry.get()
        lastName = last_name_entry.get()
        final_client = firstName+" "+lastName
        birthday = final_result.get()
        phoneNumber = phone_number_entry.get()
        email = email_entry.get()
        email.lower()
        hairCutFrequency = hair_cut_frequency_entry.get()
        hairCutStyle = hair_cut_style_entry.get()
        hairProducts = hair_products_combobox.get()
        barberName = barber_name_entry.get()
        barberName.title()
        alternaveServices = alternave_services_combobox.get()
        observations = observations_entry.get()
        observations.capitalize()
        #attendances = datetime.date.today()
        #print(f"Nombre: {firstName} {lastName}   fecha de nacimiento: {birthday} ")
        #print(f"Tel. {phoneNumber}   Correo Electronico: {email}")
        #print(f"Frecuencia de corte: {hairCutFrequency}  Productos ocurrentes: {hairProducts}")
        #print(f"Corte: {hairCutStyle}   Barbero: {barberName}")
        #print(f"Servios alternos: {alternaveServices}  observaciones: {observations}")
        addingdatabase(final_client,barberName,hairCutStyle,hairProducts,birthday,phoneNumber,observations,email,alternaveServices,hairCutFrequency)



    #Main Window
    newclientWindow = tkr.Toplevel()
    newclientWindow.title("Registrar un Nuevo Cliente ") 
    newclientmainframe = ttk.Frame(newclientWindow);
    newclientmainframe.pack()


    ##########################Client information #################################
    client_info_frame = ttk.LabelFrame(newclientmainframe,text="Información del Cliente")
    client_info_frame.grid(row=0,column=0,sticky="news", padx=20,pady=10)


    first_name_label = ttk.Label(client_info_frame,text="Nombre: ")
    first_name_label.grid(row=0,column=0)
    first_name_entry = ttk.Entry(client_info_frame)
    first_name_entry.grid(row=1,column=0)

    last_name_label = ttk.Label(client_info_frame,text="Apellído: ")
    last_name_label.grid(row=0,column=1)
    last_name_entry = ttk.Entry(client_info_frame)
    last_name_entry.grid(row=1,column=1)


    final_result = tkr.StringVar()
    birthday_label = ttk.Label(client_info_frame,text="Fecha de Nacimiento: ")
    birthday_label.grid(row=0,column=3)
    birthday_entry = DateEntry(client_info_frame,selectmode="day",textvariable=final_result)
    birthday_entry.grid(row=1, column= 3, padx=20)

    phone_number_label = ttk.Label(client_info_frame,text="Numero Telefonico: ")
    phone_number_label.grid(row=2 ,column=0)
    phone_number_entry = ttk.Entry(client_info_frame)
    phone_number_entry.grid(row=3,column=0)

    email_label = ttk.Label(client_info_frame,text="Correo Electronico:")
    email_label.grid(row=2,column=1)
    email_entry = ttk.Entry(client_info_frame)
    email_entry.grid(row=3,column=1)

    for widget in client_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5);

    ######################### #Barber Information #########################

    barber_information = ttk.LabelFrame(newclientmainframe,text="Información del Corte")
    barber_information.grid(row=1,column=0,sticky="news", padx=20,pady=10)

    hair_cut_style_label = ttk.Label(barber_information,text="Estilo de Corte: ")
    hair_cut_style_label.grid(row=0,column=0)
    hair_cut_style_entry = ttk.Entry(barber_information)
    hair_cut_style_entry.grid(row=1,column=0);

    hair_cut_frequency_label=ttk.Label(barber_information,text="Frecuencia de Corte: ")
    hair_cut_frequency_label.grid(row=0,column=1)
    hair_cut_frequency_entry = ttk.Entry(barber_information)
    hair_cut_frequency_entry.grid(row=1,column=1)

    hair_products_label = ttk.Label(barber_information,text="Productos Utilizados: ")
    hair_products_label.grid(row=0,column=2);
    hair_products_combobox = ttk.Combobox(barber_information, values=hair_products_list)
    hair_products_combobox.grid(row=1,column=2)

    barber_name_label = ttk.Label(barber_information,text="Nombre del Barbero")
    barber_name_label.grid(row=2,column=0)
    barber_name_entry = ttk.Combobox(barber_information, values=["Salvador Venegas","Lalo","Otro..."])
    barber_name_entry.grid(row=3,column=0)

    alternave_services_label = ttk.Label(barber_information,text="Servicios Alternos")
    alternave_services_label.grid(row=2,column=1)
    alternave_services_combobox = ttk.Combobox(barber_information, values=alternave_services_json)
    alternave_services_combobox.grid(row=3,column=1)



    for widget in barber_information.winfo_children():
        widget.grid_configure(padx=10,pady=5);


    ############ OBSERVATIONS ###########

    client_observations_frame = ttk.LabelFrame(newclientmainframe,text="Observaciones del Cliente")
    client_observations_frame.grid(row=3,column=0,sticky="news", padx=20,pady=10)

    observations_label = ttk.Label(client_observations_frame,text="Observaciones :")
    observations_label.grid(row=0,column=0)
    observations_entry = ttk.Entry(client_observations_frame)
    observations_entry.grid(row=1,column=0)
    for widget in client_observations_frame.winfo_children():
        widget.grid_configure(padx=100,pady=5);

    #####     BUTTONS     #####
    submtion_button = ttk.Button(newclientmainframe,text="Enviar Datos",command=submtion_data)
    submtion_button.grid(row=0,column=2,sticky="news",padx=20,pady=20)

    menu_button = ttk.Button(newclientmainframe,text="Menu Principal",command=lambda: returntomenu(newclientWindow))
    menu_button.grid(row=1,column=2,sticky="news",padx=20,pady=20)

    newclientWindow.protocol("WM_DELETE_WINDOW",endcode)

    #exit_button = tkr.Button(newclientmainframe,text="Salir",command=ebf);
    #exit_button.grid(row=2,column=2,sticky="news",padx=20,pady=20) 

    newclientWindow.mainloop()





def mainmenu():
    global window 
    ##### ROOT FRAME ####
    window = tkr.Tk();
    window.title("Barberia JLU - Menu -")
    # DEFUALT THEME ###
    theme_style = ttk.Style(window)
    window.tk.call("source","forest-dark.tcl")
    window.tk.call("source","forest-light.tcl")
    theme_style.theme_use("forest-dark")
    
    frame = ttk.Frame(window)
    frame.pack()

    ########## IMAGES FRAMES ############
    barberframe = ttk.Frame(frame)
    barberframe.grid(row=0,column=0,padx=10,pady=10)

    barberimg = tkr.PhotoImage(file="images/1.png")
    imageadjust = barberimg.subsample(3,3)
    lblbarberimg = tkr.Label(barberframe,image= imageadjust)
    lblbarberimg.grid(row=0,column=0,sticky="news",padx=10,pady=10)

    jluimg = tkr.PhotoImage(file="images/jl.png");
    jluadjust = jluimg.subsample(5,5)
    jlubarberimg = tkr.Label(barberframe,image= jluadjust)
    jlubarberimg.grid(row=0,column=3,sticky="news",padx=10,pady=10)

    ################### BUTTONS FRAME #####################
    mainFrame = ttk.Frame(frame)
    mainFrame.grid(row=1,column=0,padx=10,pady=10);

    newclientregister = ttk.Button(mainFrame, text= "Nuevo Cliente",command=lambda: submition_button(window))
    newclientregister.grid(row=0,column=0,sticky="news",padx=20,pady=20);

    mode_switch = ttk.Checkbutton(mainFrame,text="Apariencia",style="Switch",command=lambda: theme_mode(mode_switch,theme_style))
    mode_switch.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")

    lookup_button = ttk.Button(mainFrame,text="Busqueda de Cliente",command=lookupclient_button)
    lookup_button.grid(row=0,column=2,sticky="news",padx=20,pady=20)

    exitbutton = ttk.Button(mainFrame,text="Salir",command=endcode)
    exitbutton.grid(row=1,column=2,sticky="news",padx=20,pady=20);
    window.protocol("WM_DELETE_WINDOW",endcode)

    window.mainloop()


    
mainmenu()