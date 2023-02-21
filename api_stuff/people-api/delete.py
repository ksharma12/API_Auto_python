import requests

url = "http://0.0.0.0:5000//api/people/6"

payload={}
headers = {
  'Accept': 'text/html'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)