import requests
import json

URL = "http://127.0.0.1:8000/stu_create/"

data = {
    'name' : 'abdul hadi',
    'roll' : 789011,
    'city' : 'Karachi',
}

json_data = json.dumps(data)
r = requests.post(url = URL, data=json_data)
data1 = r.json()
print(data1)
