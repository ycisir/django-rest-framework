import json
import requests

URL = 'http://127.0.0.1:8000/student-api/'

def get_data(id=None):
    data = {}
    
    if id is not None:
        data = {'id':id}

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    req = requests.get(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data)

# get_data()
get_data(1)


def post_data():
    data = {
        'name': 'Draco',
        'roll': 14 ,
        'city': 'Azkaban'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    req = requests.post(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data)

# post_data()


def update_data():
    data = {
        'id': 2,
        'name':'Harry',
        'city':'Azkaban',
    }

    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    req = requests.put(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data)

# update_data()


def delete_data():
    data = {'id': 7}

    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    req = requests.delete(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data)

# delete_data()