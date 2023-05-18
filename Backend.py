import json
import tkinter
import json
import time 

def RepeatedClient (ClientName):
    with open("database.json", "r") as file:
        main = json.load(file)
    JsonList = main;
    for i in JsonList:
        if(i.get("Nombre del cliente") == ClientName):
           return True
        elif (i.get('Nombre del Cliente') != ClientName):
           return False




def NewClient(client,barber,style,products,birthday,phoneNumber,observations,email,services,frequency):
    client.title()
    Parameter = RepeatedClient(client)
    print(client)
    if Parameter == False:
        barber.title();
        style.capitalize();
        products.title();
        observations.capitalize();
        email.lower();
        barber.title()
        try:
            with open("database.json", "r") as file:
                main = json.load(file)
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
        try:
            data = {
                "Nombre del cliente" : client,
                "Nombre del Barbero" : barber,
                "Cumple" : birthday,
                "Whatsapp" : phoneNumber,
                "Estilo de corte" : style,
                "Frecuencia de corte" : frequency,
                "Productos que usa" : products,
                "Servicios alternos" : services,
                "Observaciones" : observations,
                "Correo Electronico": email
            }
            main.append(data)
            with open("database.json", "w") as file:
                json.dump(main,file,indent=4)
        except:
            print("No fue possible agregar al cliente.")


    elif True:  
        print("Cliente repetido")
        #return menu()  

    else:
        print("Upss error.")





def Lookup ():

    print("Deseas buscar al cliente por: \n1.Nombre\n2.Numero de Telefono\n")
    Option=input(">>> ")
    if(Option == 1):
        with open("database.json", "r") as file:
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
        with open("database.json", "r") as file:
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
 
