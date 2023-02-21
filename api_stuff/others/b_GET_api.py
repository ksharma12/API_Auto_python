import requests

url = "https://reqres.in/api/users?page=2"

response = requests.request(method="GET",url=url)

print(response.text)
print(response.json())
