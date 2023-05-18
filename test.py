import json

def RepeatedClient (ClientName):
    with open("database.json", "r") as file:
        main = json.load(file)
    JsonList = main;
    for i in JsonList:
        if(i.get("Nombre del cliente") == ClientName):
             print("nel")
        else:
             
            
        

var = RepeatedClient("Alexis Ortiz")








def save ():
    if (i.get('Nombre del Cliente') == f"{ClientName}"):
           return True
    else:
        print(JsonList)
        return False