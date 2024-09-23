import json
import requests

url = "http://127.0.0.1:8000/put_student/10070"

data = {
    "name" : "Hamid"
}
json_data = json.dumps(data)
r = requests.put(url = url, data = json_data)
print(r)