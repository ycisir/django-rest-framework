import json
import requests

URL = 'http://127.0.0.1:8000/student/'

def get_data(id=None):
    data = {}
    
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    req = requests.get(url=URL, data=json_data)
    data = req.json()
    print(data)

# get_data()
# get_data(9)


def post_data():
    data = {
        'name': 'Draco',
        'roll': 14 ,
        'city': 'Azkaban'
    }

    json_data = json.dumps(data)
    req = requests.post(url=URL, data=json_data)
    data = req.json()
    print(data)

post_data()


def update_data():
    data = {
        'id': 2,
        'name':'Harry',
        'city':'Azkaban',
    }

    json_data = json.dumps(data)
    req = requests.put(url=URL, data=json_data)
    data = req.json()
    print(data)

# update_data()


def delete_data():
    data = {'id': 7}

    json_data = json.dumps(data)
    req = requests.delete(url=URL, data=json_data)
    data = req.json()
    print(data)

# delete_data()