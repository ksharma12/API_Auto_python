import requests
import json

url = "http://0.0.0.0:5000//api/people/4"

payload = json.dumps({
  "fname": "Amit",
  "lname": "Saxena"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)