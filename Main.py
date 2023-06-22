import json

local = str(input())

with open(local, "r") as file:
    alternave_services_json = json.load(file)
print(alternave_services_json)



