import requests
import json

url = "http://127.0.0.1:8000/del_student/10070"
r = requests.delete(url = url)
print(r.json())