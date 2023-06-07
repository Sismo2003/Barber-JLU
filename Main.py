import json


with open("database.json", "r") as file:
    main = json.load(file)
    JsonList = main;

lista = [list(JsonList.values()) for JsonList in JsonList]

print(lista)