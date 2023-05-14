import json
import tkinter
import json
import time 





def RepeatedClient (ClientName):
    with open("database.json", "r") as file:
        main = json.load(file)
    JsonList = main;
    for i in JsonList:
        if (i.get('Nombre del Cliente') == f"{ClientName}"):
           return False
        else:
           return True

def NewClient():

    client = input(("cliente: "))
    client.title()
    Parameter = RepeatedClient(client)

    if Parameter == False:

        barber = input("Barbero: ")
        barber.title();
        birthday = input("Cumpleaños: ")
        PhoneNumber = input("Whatsapp: ")
        email = input("Correo: ")
        style = input(("Estilo de corte: "))
        style.lower();
        frecuency = input("Frecuencia de corte: ")
        products = input("Productos que usa: ")
        products.title()
        serves = input("servicios alternos: ")
        observations = input("Observaciones: ")
        

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
                "Whatsapp" : PhoneNumber,
                "Estilo de corte" : style,
                "Frecuencia de corte" : frecuency,
                "Productos que usa" : products,
                "Servicios alternos" : serves,
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
 

def Windowadding ():
        
    window = tkinter.Tk()
    window.geometry("1080x900")

    title = tkinter.Label(window, text="Barberia JLU", font="30")
    title.pack()


    addclientButon = tkinter.Button(window, text="Nuevo Cliente", padx= 20 , pady = 10, command= NewClient)
    addclientButon.pack()

    Clientboxtext = tkinter.Entry(window)
    Clientboxtext.pack()

    window.mainloop()

Windowadding()