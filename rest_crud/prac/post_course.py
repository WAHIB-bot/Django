import requests
import json

url = 'http://127.0.0.1:8000/post_student/'

data = {
    "roll" : "10070",
    "name" : "Zain",
    "city" : "Lahore",
}
json_data = json.dumps(data)
r = requests.post(url = url, data = json_data)
print(r.json())
