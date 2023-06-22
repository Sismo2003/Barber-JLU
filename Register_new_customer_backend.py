import json
from tkinter import *
import json
import time 
from tkinter import messagebox
import datetime




def RepeatedClient (ClientName,PhoneNumber,email):
    try:
        with open("config.json","r") as file:
            path = json.load(file);
    except:
        print("La dirrecion de la base de datos no existe.")
    ########################################
    try:
        with open(path.get("DatabasePath"), "r") as file:
            main = json.load(file)
        JsonList = main;
    except:
        print("error al cargar la base de datos")
    flag = False
    for i in JsonList:
        if(i.get('Nombre del Cliente') == ClientName or i.get('Whatsapp') == PhoneNumber and i.get('Correo Electronico') == email):
            flag = True
    if(flag):
        return True
    else:
        return False


def addingdatabase(client,barber,style,products,birthday,phoneNumber,observations,email,services,frequency):
    try:
        with open("config.json","r") as file:
           path = json.load(file);
    except:
        print("La dirrecion de la base de datos no existe.")
    
    try:
        client = client.title();
        barber = barber.title();
        style = style.capitalize();
        products = products.title();
        observations =observations.capitalize();
        email = email.lower();
        barber = barber.title();
        frequency = frequency.title();
        todayday = datetime.date.today()
        last_visit = f"{todayday}"
        Parameter = RepeatedClient(client,phoneNumber,email)
    except:
        messagebox.showwarning("Error al encontrar la base de datos.", "La base de datos no fue encontrada, revisa que exista en tus archivos.")

    if Parameter == False:
        try:
            with open(path.get("DatabasePath"), "r") as file:
                main = json.load(file)
        except:
             messagebox.showwarning("Error al encontrar la base de datos.", "La base de datos no fue encontrada, revisa que exista en tus archivos.")
        try:
            data = {
                "Nombre del Cliente" : client,
                "Fecha de Nacimiento" : birthday,
                "Whatsapp" : phoneNumber,
                "Correo Electronico": email,
                "Nombre del Barbero" : barber,
                "Estilo de Corte" : style,
                "Frecuencia de Corte" : frequency,
                "Productos Utilizados" : products,
                "Servicios Alternos" : services,
                "Observaciones" :observations,
                "Visitas" : last_visit
            }
            main.append(data)
            with open(path.get("DatabasePath"), "w") as file:
                json.dump(main,file,indent=4)
        except:
            messagebox.showwarning("Error en la Base De Datos","No fue possible agregar al cliente.")


    elif True:  
        messagebox.showwarning("Cliente Repetido","Actualmente existe un cliente con la misma información digitada, trata de editar la información del cliente.",)


def Lookup ():
    try:
        with open("config.json","r") as file:
           path = json.load(file);
    except:
        print("La dirrecion de la base de datos no existe.")
    
    print("Deseas buscar al cliente por: \n1.Nombre\n2.Numero de Telefono\n")
    Option=input(">>> ")
    if(Option == 1):
        with open(path.get("DatabasePath"), "r") as file:
            main = json.load(file)
        JsonList = main;
        try: 
            Search = input("Ingrese el Nombre del cliente a buscar: ")
            for i in JsonList:
                if (i.get('Nombre del Cliente') == f"{Search}"):
                    print (i)
                else:
                    print("El cliente no exite")
        except:
            print("Error la lista de clientes esta vacia.")

    elif(Option == 2 ):
        with open(path.get("DatabasePath"), "r") as file:
            main = json.load(file)
            JsonList = main;
        try: 
            Search = input("Ingrese el Telefono del cliente a buscar: ")
            for i in JsonList:
                if (i.get('Whatsapp') == f"{Search}"):
                    print (i)
                else:
                    print("El cliente no exite")
        except:
            print("Error la lista de clientes esta vacia.")
 
