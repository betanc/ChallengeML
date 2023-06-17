import requests
import json

url = "https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"

response = requests.get(url)
data = response.json()

with open(datos.json, w) as file:
     json.dump(data, file)

