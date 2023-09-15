import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


# get Student Data

def get_data(id = None):
    data = {}
    if id is not None:
        data= {'id' : id}
    json_data = json.dumps(data)    
    headers = {'content-Type': 'application/json'}
    response_data = requests.get(url=URL, headers=headers, data= json_data)
    data = response_data.json()
    print(data)
# get_data() 


# create student data


def post_data():
    data = {
        'name' : 'suman',
        'roll' : 106,
        'city' : 'indore'
    }
    headers = {'content-Type': 'application/json'}
    
    json_data = json.dumps(data)
    response_data = requests.post(url = URL, headers= headers, data = json_data)
    data = response_data.json()
    print(data)

# post_data() 


# update Student data

def update_data():
    data = {
        'id' : 6,
        'name' : 'sachin',
        'roll' : 102,
        'city' : 'america'
    }
    headers = {'content-Type': 'application/json'}    
    
    json_data = json.dumps(data)
    response_data = requests.put(url = URL, headers=headers ,data = json_data)
    data = response_data.json()
    print(data)

# update_data()


# delete student data

def delete_data():
    data = {'id' : 6 }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}    
    response_data = requests.delete(url = URL, headers=headers, data = json_data)
    data = response_data.json()
    print(data)
delete_data()