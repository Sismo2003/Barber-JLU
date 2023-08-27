import json
from tkinter import *
import json
import time 
from tkinter import messagebox
import datetime
FlagCounter = 0;
def loadDatabase():
    try:
        with open("config.json","r") as file:
            path = json.load(file);
        with open(path.get("DatabasePath"), "r") as file:
            main = json.load(file)
        return(path,main)
    except:
        messagebox.showerror(title="Err0r 00xf1", Message="Error en las bases de datos.")
        


def RepeatedClient (ClientName,PhoneNumber,email):

    path, main = loadDatabase()
    flag = False
    JsonList = main;
    for i in JsonList:
        if(i.get('Nombre del Cliente') == ClientName or i.get('Whatsapp') == PhoneNumber and i.get('Correo Electronico') == email):
            flag = True
    if(flag):
        return True
    else:
        return False


def addingdatabase(client,barber,style,products,birthday,phoneNumber,observations,email,services,frequency):
    errorFlag = False;
    try:
        path, main = loadDatabase() 
    except:
        return 0
    
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

    
    try: 
        if Parameter == False:
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
                "Visitas" : 1,
                "Registro" : last_visit
            }
            main.append(data)
            with open(path.get("DatabasePath"), "w") as file:
                json.dump(main,file,indent=4)
                return 1;
        else:  
            return 2;
    except:
        errorFlag = True;

    
    
def updateClientInfo(IDNAME,client,barber,style,products,birthday,phoneNumber,observations,email,services,frequency,visitas):
    path, main = loadDatabase()
    clientExist = False;
    print(IDNAME)
    for entry in main:
        if entry["Nombre del Cliente"] == IDNAME:
            entry["Nombre del Cliente"] = client
            entry["Fecha de Nacimiento"] = birthday
            entry["Whatsapp"] = phoneNumber
            entry["Correo Electronico"] = email
            entry["Nombre del Barbero"] = barber
            entry["Estilo de Corte"] = style
            entry["Frecuencia de Corte"] = frequency
            entry["Servicios Alternos"] = services
            entry["Observaciones"] = observations
            entry["Visitas"] = visitas
            clientExist = True;
            break
    if(clientExist == True): 
        with open(path.get("DatabasePath"), "w") as file:
            json.dump(main,file,indent=4)
        return 1;
    else:
        return 0;
            
    
def DeleteClient(name):

    path, main = loadDatabase()

    dataUpdate = [entry for entry in main if entry["Nombre del Cliente"] != name]
    with open(path.get("DatabasePath"), "w") as file:
        json.dump(dataUpdate,file,indent=4)  
        
            
            
            
            
            
            
            
            