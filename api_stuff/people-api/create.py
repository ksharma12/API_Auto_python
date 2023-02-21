import requests
import json

url = "http://0.0.0.0:5000//api/people"

payload = json.dumps({
    "fname": "Tina",
    "lname": "Sachdeva"
})
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
