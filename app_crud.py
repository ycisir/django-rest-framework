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

get_data(1)