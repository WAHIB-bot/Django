import requests
import json

URL = "http://127.0.0.1:8000/course//student//enroll"

# json_data = json.dumps(data)
r = requests.post(url = URL)