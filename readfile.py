import json 

# file = open("D:\data\devices.json","r")
file = open("devices.json","r")
x = file.read()

finaldata= json.loads(x)

print(finaldata)