# 3rd party python application that get data using our api
# make sure your server is running
# sending backend data to frontend in json type

import requests

URL = 'http://127.0.0.1:8000/student-info/1'
# URL = 'http://127.0.0.1:8000/student-info'

req = requests.get(url=URL)
data = req.json()
print(data)