main = [{"nombre": "AlexisOrtiz", "edad":"100"},{"nombre": "juan", "edad":"1"}]

for value in main:
    if(value["nombre"] == "juan"):
        numero = int(value["edad"])
        numero += 1;
        numero = str(numero)
        value["edad"] = numero;
        username = value["nombre"]

print(username)
