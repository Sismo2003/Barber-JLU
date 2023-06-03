import json
from tkinter import *
import json
import time 
from tkinter import messagebox
import datetime


def Lookup (howtolookup,userentry):
    try:
        with open("database.json", "r") as file:
            main = json.load(file)
        JsonList = main;
    except:
        messagebox.showerror()("Error en la base de datos","La base de datos no se puedo leer correctamente.");
    if(howtolookup == 1):
        try: 
            flag = False;
            information = {}
            clientscount = 0
            for i in JsonList:
                if (i.get('Nombre del cliente') == userentry):
                    flag = True;
                    information = i;
                    ++clientscount;
                else:
                    flag = False;
            if(flag == True):
                return information,clientscount;
            else:
                return False
        except:
            messagebox.showerror("Error en la busqueda del cliente","Hubo un error al buscar en la base de datos.");


    elif(howtolookup == 2 ):
        try: 
            flag = False;
            information = {};
            clientscount = 0;
            for i in JsonList:
                if (i.get('Whatsapp') == userentry):
                    flag = True
                    information = 
                else:
                    print("El cliente no exite")
        except:
            print("Error la lista de clientes esta vacia.")
 
Lookup(1, "Alexis Ortiz")