import requests
import json

url = "https://reqres.in/api/users"
# queryParams = {"name": "asdf",
#               "key": "wwerfhdbvdjvndvjbdcjdvn",
#               "token": "2742hf3bfefbu3u3fbehfbdhdvdv"}

#response = requests.request("POST", url, params=queryParams)
response = requests.request("POST",url)

print(response.json()["id"])
print(response.json()["createdAt"])
print(response.request.url)
print(response.request.body)
print(response.request.headers)
print(response.request.method)
print(response.request.path_url)
print(response.text)
print(response.status_code)


assert response.status_code == 201
