import requests
import json

api_url = "https://fakerapi.it/api/v1/users?_quantity=5"

# Realiza la solicitud GET a la API
response = requests.get(api_url)

# Cargar la respuesta JSON en un diccionario de Python
if response.status_code == 200:
    # Utilizar json.loads para cargar el contenido de la respuesta
    data = json.loads(response.text)
    for userData in data['data']:
        print(f"User {userData['id']}")
        print(f"Username: {userData['username']}")
        print(f"Password: {userData['password']}")
        print(f"Email: {userData['email']}")
        print(f"IP: {userData['ip']}")
        print(f"Mac-Address: {userData['macAddress']}")
        print(f"Web Site: {userData['website']}")
        print("\n\n")
else:
    print(f"Error: {response.status_code}")


