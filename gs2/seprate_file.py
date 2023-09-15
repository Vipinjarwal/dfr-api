import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name' : 'kishan',
    'roll' : 101,
    'city' : 'pune'
} 

json_data = json.dumps(data)

response_data = requests.post(url = URL, data = json_data)

show_data = response_data.json()

print(show_data)