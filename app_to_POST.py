# 3rd party python application that POST data using our api
# make sure your server is running
# sending data from frontend in json type to backend

import requests
import json

URL = 'http://127.0.0.1:8000/create/'

data = {
    'name': 'Ron',
    'roll': 18,
    'city': 'Somewhere'
}

json_data = json.dumps(data)
req = requests.post(url=URL, data=json_data)
data = req.json()
print(data)