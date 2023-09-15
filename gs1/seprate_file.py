import requests

URL = "http://127.0.0.1:8000/stuinfo/3"

response_data = requests.get(url= URL)

json_data = response_data.json()

print(json_data)
