import json
import tkinter as tkr
import json
import datetime
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import time
from Register_new_customer_backend import *

def endcode():
    exit()
    
 
def ebf ():
    messagebox.showwarning("Cierre de programa","Estas apunto de cerrar el programa, estas actualmente ingresando los datos de un cliente.")
    exit();
    
def on_focusOut (event,variable ,text1):
    if variable.get() == "":
        variable.insert(0,text1)


def on_focuIn(event, variable, text1):
    if variable.get() == text1:
        variable.delete(0,"end")

def returntomenu (winclose):
    winclose.destroy()


def load_data (treeview,toppinglist):
    try:
        with open("config.json","r") as file:
           path = json.load(file);
    except:
        messagebox.showerror(message="Error al cargar la base de datos.",title="Carga de base de datos error")
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
        messagebox.showerror(message="Error al cargar la base de datos.",title="Carga de base de datos error")
        return True
        




def ClientEdit(record):
    def submtion_data():
        firstName = first_name_entry.get()
        birthday = final_result.get()
        phoneNumber = phone_number_entry.get()
        phoneNumber = str(phoneNumber)
        record02 = str(record[2])
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
        frequency = client_frequency_spinbox.get()
        frequency = str(frequency)
        record10 = str(record[10])
        # phoneNumber != record[2]
        if(firstName != record[0]  or email != record[3] or birthday != record[1] or phoneNumber != record02
            or hairCutFrequency != record[6] or hairProducts != record[7] or barberName != record[4] or  
            alternaveServices != record[8] or observations != record[9] or hairCutStyle != record[5] or frequency != record10):

            mssg = messagebox.askquestion(message=f"Deseas guardar la nueva informacion del cliente {record[0]}",title="Confirmacion")
            if(mssg == "yes"):
                answer = updateClientInfo(record[0],firstName,barberName,hairCutStyle,hairProducts,birthday,phoneNumber,observations,email,alternaveServices,hairCutFrequency,frequency)
                if(answer == 1):
                    messagebox.showinfo(title="Registro con exito",message=f"El cliente {record[0]} fue actualizado con exito!")
                    returnTopObject()
                elif(answer == 0):
                    messagebox.showerror(title="Registro fallido", message="El cliente no fue actulizado con exito.")
        else:
           mssgbox =  messagebox.askquestion(title="Actualizacion del cliente", message=f"No se registro ninguna modificacion al cliente ' {record[0]} ', Deseas volver a la vista de clientes? ")
           if mssgbox == "yes":
               returnTopObject()
            

    def DeleteClientConfirm():
        msgbox =  messagebox.askquestion(title="Borrar registro", message=f"Estas seguro que deseas borrar el cliente \"{record[0]}\"  de la base de datos?  (no habra regreso.)")
        deleteSuccess = False;
        try:
            if(msgbox == "yes"):
                DeleteClient(record[0])
                deleteSuccess = True;
        except:
           messagebox.showerror(title="Error fx(0983DCC)", message="Error al intentar borrar al cliente.")
        if(deleteSuccess):
            messagebox.showinfo(message="El cliente fue borrado con exito.")
            returnTopObject()
            
    def returnTopObject():
        top.destroy()
        lookupclient_button()
    
    top = tkr.Toplevel()
    
    top.resizable(False, False)
    top.title("Edicion de datos")
    frame = ttk.Frame(top)
    frame.pack()
    wetdgeFrame = ttk.Frame(frame)
    wetdgeFrame.pack()
    client_info_frame = ttk.LabelFrame(wetdgeFrame,text="Información del Cliente")
    client_info_frame.grid(row=0,column=0,sticky="news", padx=20,pady=10)


    first_name_label = ttk.Label(client_info_frame,text="Nombre: ")
    first_name_label.grid(row=0,column=0)
    first_name_entry = ttk.Entry(client_info_frame)
    first_name_entry.insert(0,f"{record[0]}")
    first_name_entry.grid(row=1,column=0)


    final_result = tkr.StringVar()
    birthday_label = ttk.Label(client_info_frame,text="Fecha de Nacimiento: ")
    birthday_label.grid(row=0,column=3)
    birthday_entry = DateEntry(client_info_frame,selectmode="day",textvariable=final_result)
    birthday_entry.delete(0,"end")
    birthday_entry.insert(0,f"{record[1]}")
    birthday_entry.grid(row=1, column= 3, padx=20)

    phone_number_label = ttk.Label(client_info_frame,text="Numero Telefonico: ")
    phone_number_label.grid(row=0 ,column=1)
    phone_number_entry = ttk.Entry(client_info_frame)
    phone_number_entry.insert(0,record[2])
    phone_number_entry.grid(row=1,column=1)

    email_label = ttk.Label(client_info_frame,text="Correo Electronico:")
    email_label.grid(row=2,column=0)
    email_entry = ttk.Entry(client_info_frame)
    email_entry.insert(0,f"{record[3]}")
    email_entry.grid(row=3,column=0)

    for widget in client_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5);

    ######################### #Barber Information #########################

    barber_information = ttk.LabelFrame(wetdgeFrame,text="Información del Corte")
    barber_information.grid(row=1,column=0,sticky="news", padx=20,pady=10)

    barber_name_label = ttk.Label(barber_information,text="Nombre del Barbero")
    barber_name_label.grid(row=2,column=0)
    barber_name_entry = ttk.Combobox(barber_information, values=["Salvador Venegas","Lalo","Otro..."])
    barber_name_entry.insert(0,f"{record[4]}")
    barber_name_entry.grid(row=3,column=0)

    hair_cut_style_label = ttk.Label(barber_information,text="Estilo de Corte: ")
    hair_cut_style_label.grid(row=0,column=0)
    hair_cut_style_entry = ttk.Entry(barber_information)
    hair_cut_style_entry.insert(0,f"{record[5]}")
    hair_cut_style_entry.grid(row=1,column=0);

    hair_cut_frequency_label=ttk.Label(barber_information,text="Frecuencia de Corte: ")
    hair_cut_frequency_label.grid(row=0,column=1)
    hair_cut_frequency_entry = ttk.Entry(barber_information)
    hair_cut_frequency_entry.insert(0,f"{record[6]}")
    hair_cut_frequency_entry.grid(row=1,column=1)

    with open("hair_products.json", "r") as file:
        hair_products_list = json.load(file)

    with open("alternave_services.json", "r") as file:
        alternave_services_json = json.load(file)
        
    hair_products_label = ttk.Label(barber_information,text="Productos Utilizados: ")
    hair_products_label.grid(row=0,column=2);
    hair_products_combobox = ttk.Combobox(barber_information, values=hair_products_list)
    hair_products_combobox.insert(0,f"{record[7]}")
    hair_products_combobox.grid(row=1,column=2)


    alternave_services_label = ttk.Label(barber_information,text="Servicios Alternos")
    alternave_services_label.grid(row=2,column=1)
    alternave_services_combobox = ttk.Combobox(barber_information, values=alternave_services_json)
    alternave_services_combobox.insert(0,f"{record[8]}")
    alternave_services_combobox.grid(row=3,column=1)



    for widget in barber_information.winfo_children():
        widget.grid_configure(padx=10,pady=5);


    ############ OBSERVATIONS ###########

    client_observations_frame = ttk.LabelFrame(wetdgeFrame,text="Observaciones del Cliente")
    client_observations_frame.grid(row=2,column=0,sticky="news", padx=20,pady=10)

    observations_label = ttk.Label(client_observations_frame,text="Observaciones:")
    observations_label.grid(row=0,column=0,padx=5)
    observations_entry = ttk.Entry(client_observations_frame)
    observations_entry.insert(0,f"{record[9]}")
    observations_entry.grid(row=1,column=0,padx=5,pady=20)
    
    client_frequency_label = ttk.Label(client_observations_frame,text="Visitas:")
    client_frequency_label.grid(row=0,column=1)
    client_frequency_spinbox = ttk.Spinbox(client_observations_frame, from_=1, to=100)
    client_frequency_spinbox.insert(0,f"{record[10]}")
    client_frequency_spinbox.grid(row=1,column=1,padx=20,pady=20)
    
    
    
    #for widget in client_observations_frame.winfo_children():
     #   widget.grid_configure(padx=100,pady=5);

    
    submtion_button = ttk.Button(wetdgeFrame,text="Guardar Registro",command=submtion_data)
    submtion_button.grid(row=0,column=1,sticky="news",padx=20,pady=20)

    erase_buttom = ttk.Button(wetdgeFrame,text="Borrar Registro",command=DeleteClientConfirm)
    erase_buttom.grid(row=1,column=1,sticky="news",padx=20,pady=20)
    
    menu_button = ttk.Button(wetdgeFrame,text="Salir",command=returnTopObject)
    menu_button.grid(row=2,column=1,sticky="news",padx=20,pady=20)

    wetdgeFrame.mainloop();


def lookupclient_button():


    def item_select():
        selected_item = treeview_y.focus()
        if selected_item:
            item = treeview_y.item(selected_item)
            record = item['values']
            showdatawindow.destroy()
            ClientEdit(record)
        else:
            messagebox.showerror(title="Cliente no seleccionado",message="Selecciona un cliente para poder editarlo.")
            #msgbox =  messagebox.askquestion(title="Cliente registrado con exito", message=f"El cliente \" {firstName} {lastName} \"  Fue registrado con exito. Deseas volver al menu principal?")



    showdatawindow = tkr.Toplevel()
    showdatawindow.title("Mostrar Cliente");
    frame = ttk.Frame(showdatawindow)
    frame.pack();
    
    lookupframe = ttk.LabelFrame(frame, text="Busqueda del cliente")  
    lookupframe.grid(row=0,column=0,padx=20,pady=20)

    name_label = ttk.Label(lookupframe,text="Nombre del Cliente")
    name_label.grid(row=0,column=0)
    name_entry = ttk.Entry(lookupframe)
    name_entry.insert(0,"Cristiano Gomes")
    name_entry.bind("<FocusIn>", lambda event :on_focuIn(event,name_entry,"Cristiano Gomes"))
    name_entry.bind("<FocusOut>",lambda event :on_focusOut(event,name_entry,"Cristiano Gomes"))
    name_entry.grid(row=1,column=0,sticky="ew",padx=20,pady=20)



    phonenumber_label = ttk.Label(lookupframe,text="Numero Telefonico")
    phonenumber_label.grid(row=2,column=0)
    phonenumber_entry = ttk.Entry(lookupframe)
    phonenumber_entry.insert(0,"+52 33 1234 5678")
    phonenumber_entry.bind("<FocusIn>",lambda event :on_focuIn(event,phonenumber_entry,"+52 33 1234 5678"))
    phonenumber_entry.bind("<FocusOut>",lambda event :on_focusOut(event,phonenumber_entry,"+52 33 1234 5678"))
    phonenumber_entry.grid(row=3,column=0,padx=20,pady=20,sticky="ew")



    email_label = ttk.Label(lookupframe,text="Correo Electronico")
    email_label.grid(row=4,column=0)
    email_entry = ttk.Entry(lookupframe)
    email_entry.insert(0,"example@dominio.com")
    email_entry.bind("<FocusIn>",lambda event :on_focuIn(event,email_entry,"example@dominio.com"))
    email_entry.bind("<FocusOut>",lambda event :on_focusOut(event,email_entry,"example@dominio.com"))
    email_entry.grid(row=5,column=0,padx=10,pady=10,sticky="ew")

    def SearchBy():
        try:
            lookupEmail = email_entry.get()
            lookupPhoneNumber = phonenumber_entry.get()
            lookupName = name_entry.get()
            lookupName = lookupName.title()
        except:
            messagebox.showwarning("Error al obtener los valores de los campos.")
        lookupFlag = False;
        noValueFound = False;
        
        if (lookupName != "Cristiano Gomes"):
            lookupFlag = True;
            column_index = 0;
            for item in treeview_y.get_children():
                item_values = treeview_y.item(item, "values")
                if item_values and len(item_values) > column_index:
                    if item_values[column_index] == lookupName:
                        treeview_y.selection_set(item) 
                        treeview_y.focus(item)
                        treeview_y.see(item)
                        noValueFound = True;
                        return

                    
        if(lookupEmail != "example@dominio.com"):
            lookupFlag = True;
            column_index = 3;
            for item in treeview_y.get_children():
                item_values = treeview_y.item(item, "values")
                if item_values and len(item_values) > column_index:
                    if item_values[column_index] == lookupEmail:
                        treeview_y.selection_set(item) 
                        treeview_y.focus(item)
                        treeview_y.see(item)
                        noValueFound = True;
                        return

  
            
        if(lookupPhoneNumber != "+52 33 1234 5678"):
            lookupFlag = True;
            column_index = 2;
            for item in treeview_y.get_children():
                item_values = treeview_y.item(item, "values")
                if item_values and len(item_values) > column_index:
                    if item_values[column_index] == lookupPhoneNumber:
                        treeview_y.selection_set(item) 
                        treeview_y.focus(item)
                        treeview_y.see(item)
                        noValueFound = True;
                        return
               
        
                
        if (lookupFlag == False):
            noValueFound = True;
            messagebox.showerror(title="Busqueda Invalida", message="Ingrese un valor valido para buscar en la base de datos")    
        
        if  (noValueFound == False):
            messagebox.showerror(title="Busqueda Invalida", message="El cliente no existe en la base de datos.")    

            
    lookup_button = ttk.Button(lookupframe,text="Buscar",command=SearchBy)
    lookup_button.grid(row=6,column=0,sticky="nsew",padx=20,pady=20)

    
    edit_button = ttk.Button(lookupframe,text="Editar",command=item_select)
    edit_button.grid(row=7,column=0,padx=20,pady=20,sticky="NSEW")

    returntomenu_button = ttk.Button(lookupframe,text="Regresar al menu",command=lambda  :returntomenu(showdatawindow))
    returntomenu_button.grid(row=9,column=0,padx=20,pady=20,sticky="nsew")

    colms = ("Nombre","Fecha de Nacimiento","Telefono","Email","Barber","Corte","Frecuencia de corte","Productos","Servicios alternos","Observaciones","Visitas")
    
    treeframe = ttk.Frame(frame)
    treeframe.grid(row=0, column=1,padx=5, pady=5)

    treeview_y = ttk.Treeview(treeframe, show="headings", columns=colms, height=12)
    
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
    treeview_y.column("Visitas",width=60)
   

    scrollbar = ttk.Scrollbar(treeframe,orient="vertical",command=treeview_y.yview)
    treeview_y.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    treeview_y.pack()
    


    #treeview_y.bind('<<TreeviewSelect>>', item_select)
    load_data(treeview_y,colms)


    showdatawindow.resizable(False, False)
    #showdatawindow.protocol("WM_DELETE_WINDOW",endcode)
    showdatawindow.mainloop()



def theme_mode (interruptor,style):
    if interruptor.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")


def visit():
    top = tkr.Toplevel()
    top.title("Registro de visita de cliente")
    visitmainframe = tkr.Frame(top)
    visitmainframe.pack()
    
    visitmainframe.mainloop()


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
        

        answer =  addingdatabase(final_client,barberName,hairCutStyle,hairProducts,birthday,phoneNumber,observations,email,alternaveServices,hairCutFrequency)
        if(answer == 1): 
            msgbox =  messagebox.askquestion(title="Cliente registrado con exito", message=f"El cliente \" {firstName} {lastName} \"  Fue registrado con exito. Deseas volver al menu principal?")
            if(msgbox == "yes"):
                returntomenu(newclientWindow)
        elif(answer == 0):
            messagebox.showerror(title="Error 01xf2",message="Error en la base de datos.")
        elif(answer == 2):
            messagebox.showwarning("Cliente Repetido","Actualmente existe un cliente con la misma información digitada, trata de editar la información del cliente.",)

            
        
 

    #Main Window
    newclientWindow = tkr.Toplevel()
    newclientWindow.title("Registrar un Nuevo Cliente ") 
    wetdgeFrame = ttk.Frame(newclientWindow);
    wetdgeFrame.pack()
    newclientWindow.resizable(False, False)

    ##########################Client information #################################
    client_info_frame = ttk.LabelFrame(wetdgeFrame,text="Información del Cliente")
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

    barber_information = ttk.LabelFrame(wetdgeFrame,text="Información del Corte")
    barber_information.grid(row=1,column=0,sticky="news", padx=20,pady=10)

    hair_cut_style_label = ttk.Label(barber_information,text="Estilo de Corte: ")
    hair_cut_style_label.grid(row=0,column=0)
    hair_cut_style_entry = ttk.Entry(barber_information)
    hair_cut_style_entry.grid(row=1,column=0);

    hair_cut_frequency_label=ttk.Label(barber_information,text="Frecuencia de Corte: ")
    hair_cut_frequency_label.grid(row=0,column=1)
    hair_cut_frequency_entry = ttk.Entry(barber_information)
    hair_cut_frequency_entry.grid(row=1,column=1)

    with open("hair_products.json", "r") as file:
        hair_products_list = json.load(file)

    with open("alternave_services.json", "r") as file:
        alternave_services_json = json.load(file)
        
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

    client_observations_frame = ttk.LabelFrame(wetdgeFrame,text="Observaciones del Cliente")
    client_observations_frame.grid(row=3,column=0,sticky="news", padx=20,pady=10)

    observations_label = ttk.Label(client_observations_frame,text="Observaciones :")
    observations_label.grid(row=0,column=0)
    observations_entry = ttk.Entry(client_observations_frame)
    observations_entry.grid(row=1,column=0)
    for widget in client_observations_frame.winfo_children():
        widget.grid_configure(padx=100,pady=5);

    #####     BUTTONS     #####
    submtion_button = ttk.Button(wetdgeFrame,text="Enviar Datos",command=submtion_data)
    submtion_button.grid(row=0,column=2,sticky="news",padx=20,pady=20)

    menu_button = ttk.Button(wetdgeFrame,text="Menu Principal",command=lambda: returntomenu(newclientWindow))
    menu_button.grid(row=1,column=2,sticky="news",padx=20,pady=20)


    newclientWindow.mainloop()



def pathdatabase ():
    def cambiopath():
        mssgbox = messagebox.askquestion(title="Cambio de PATH base de datos", message="Estas seguro que quieres cambiar la dirrecion de la base de datos? ")
        if(mssgbox == "yes"):
            try:
                with open("config.json","r") as configfile:
                    path = json.load(configfile);
                path['DatabasePath'] = entry_base.get()
                with open("config.json","w") as configfile:
                    json.dump(path,configfile,indent=4)
                msgbox = messagebox.askquestion(title="Base de datos", message=f"La nueva dirreción de la base de dato fue registrada con EXITO. Deseas volver al menu principal?")
                if(msgbox == "yes"):
                    returntomenu(pathwindow)
            except:
                messagebox.showerror("Error al cambiar la base de datos")        
    pathwindow = tkr.Toplevel()
    pathwindow.title("Dirrecion de Base de Datos")
    pathmainframe = ttk.Frame(pathwindow)
    pathmainframe.pack()
    with open("config.json","r") as configfile:
                path = json.load(configfile);
    footer_label = ttk.Label(pathmainframe,text=f"Path: {path['DatabasePath']}")
    footer_label.grid(column=0,row=3,sticky="EN",padx=5,pady=5)

    base_text=ttk.Label(pathmainframe,text="Path")
    base_text.grid(column=0,row=0,padx=10,pady=10);
    
    entry_base = ttk.Entry(pathmainframe)
    entry_base.grid(column=0,row=1,padx=10,pady=10);
    
    
    submit_button = ttk.Button(pathmainframe,text="submit",command=cambiopath)
    submit_button.grid(column=1,row=1,padx=10,pady=10);
    
    returntomenubutton = ttk.Button(pathmainframe,text="Menu",command=lambda: returntomenu(pathwindow))
    returntomenubutton.grid(column=1,row=2,padx=10,pady=10);
    pathwindow.resizable(False, False)
    pathwindow.mainloop()


    return 0;


def VisitMark():
    top = tkr.Toplevel()
    topframe = ttk.Frame(top)
    topframe.grid(row=0,column=0)
    top.resizable(False, False)

    
    lookupframe = ttk.LabelFrame(topframe,text="Busqueda de Cliente")
    lookupframe.grid(row=0,column=0,padx=10,pady=10)
    
    
    name_label = ttk.Label(lookupframe,text="Nombre del Cliente")
    name_label.grid(row=0,column=0,pady=10)
    name_entry = ttk.Entry(lookupframe)
    name_entry.insert(0,"Cristiano Gomes")
    name_entry.bind("<FocusIn>", lambda event :on_focuIn(event,name_entry,"Cristiano Gomes"))
    name_entry.bind("<FocusOut>",lambda event :on_focusOut(event,name_entry,"Cristiano Gomes"))
    name_entry.grid(row=1,column=0,sticky="ew",padx=20,pady=10)



    phonenumber_label = ttk.Label(lookupframe,text="Numero Telefonico")
    phonenumber_label.grid(row=2,column=0,pady=5)
    phonenumber_entry = ttk.Entry(lookupframe)
    phonenumber_entry.insert(0,"+52 33 1234 5678")
    phonenumber_entry.bind("<FocusIn>",lambda event :on_focuIn(event,phonenumber_entry,"+52 33 1234 5678"))
    phonenumber_entry.bind("<FocusOut>",lambda event :on_focusOut(event,phonenumber_entry,"+52 33 1234 5678"))
    phonenumber_entry.grid(row=3,column=0,padx=20,sticky="ew",pady=10)



    email_label = ttk.Label(lookupframe,text="Correo Electronico")
    email_label.grid(row=4,column=0)
    email_entry = ttk.Entry(lookupframe)
    email_entry.insert(0,"example@dominio.com")
    email_entry.bind("<FocusIn>",lambda event :on_focuIn(event,email_entry,"example@dominio.com"))
    email_entry.bind("<FocusOut>",lambda event :on_focusOut(event,email_entry,"example@dominio.com"))
    email_entry.grid(row=5,column=0,padx=10,sticky="ew",pady=10)
    

    buttonsFrame = ttk.Frame(topframe)
    buttonsFrame.grid(row=0,column=1)
    

    def ClientConfirm():
        name = name_entry.get()
        phoneNumber = phonenumber_entry.get()
        email = email_entry.get()
        if(name != "Cristiano Gomes"):
            visitRegistration(name,1)
        elif(phoneNumber != "+52 33 1234 5678"):
            visitRegistration(phoneNumber,2)
        else:
            visitRegistration(email,0)

    
    visit_register_button = ttk.Button(buttonsFrame,text="Registrar visita",command=ClientConfirm)
    visit_register_button.grid(row=1, column=1,padx=20,pady=20)

    
    returnToMenu_button = ttk.Button(buttonsFrame,text="Menu Principal")
    returnToMenu_button.grid(row=3,column=1,padx=20,pady=20)
    
    top.mainloop()

def mainmenu():
    ##### ROOT FRAME ####
    window = tkr.Tk();
    window.resizable(False, False)
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

    labelmainframe = ttk.LabelFrame(mainFrame,text="Opciones")
    labelmainframe.grid(row=0,column=0,sticky="ns",padx=20,pady=20)


   #############################################################################################

    newclientregister = ttk.Button(labelmainframe, text= "Nuevo Cliente",command= NewClient)
    newclientregister.grid(row=0,column=0,sticky="NEWS",padx=20,pady=20);

    visitclient_button = ttk.Button(labelmainframe,text="Registrar Visita de Cliente",command=VisitMark)
    visitclient_button.grid(row=0,column=1,padx=20,pady=20,sticky="NEWS")


    lookup_button = ttk.Button(labelmainframe,text="Busqueda de Cliente",command=lookupclient_button)
    lookup_button.grid(row=1,column=0,sticky="NEWS",padx=20,pady=20)


    exitbutton = ttk.Button(labelmainframe,text="Salir",command=endcode)
    exitbutton.grid(row=1,column=1,sticky="NEWS",padx=20,pady=20);
    
    mode_switch = ttk.Checkbutton(labelmainframe,text="Apariencia",style="Switch",command=lambda: theme_mode(mode_switch,theme_style))
    mode_switch.grid(row=2,column=0,padx=20,pady=20,sticky="NEWS")

    database_location = ttk.Button(labelmainframe,text="Path Base de datos",command=pathdatabase)
    database_location.grid(row=2,column=1,sticky="NEWS",padx=10,pady=10)
    

    versionLabel = ttk.Label(frame, text="Version: Alpha 1.V")
    versionLabel.grid(row=3,column=0)
    window.protocol("WM_DELETE_WINDOW",endcode)
    

    window.mainloop()


    
mainmenu()