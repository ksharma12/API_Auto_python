import requests

url = "http://0.0.0.0:5000//api/people/4"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)