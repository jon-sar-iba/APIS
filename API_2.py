import requests
import json

api_url = "https://fakerapi.it/api/v1/persons?_quantity=5"

# Realiza la solicitud GET a la API
response = requests.get(api_url)

# Cargar la respuesta JSON en un diccionario de Python
if response.status_code == 200:
    # Utilizar json.loads para cargar el contenido de la respuesta
    data = json.loads(response.text)
    for personData in data['data']:
        print(f"Persona {personData['id']}")
        print(f"Nombre: {personData['firstname']}")
        print(f"Email: {personData['email']}")
        print(f"Telefono: {personData['phone']}")
        print(f"Fecha de nacimiento: {personData['birthday']}")
        print("\n\n")
else:
    print(f"Error: {response.status_code}")


