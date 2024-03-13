import requests
import json

api_url = "https://fakerapi.it/api/v1/places?_quantity=10"

# Realiza la solicitud GET a la API
response = requests.get(api_url)

# Cargar la respuesta JSON en un diccionario de Python
if response.status_code == 200:
    # Utilizar json.loads para cargar el contenido de la respuesta
    data = json.loads(response.text)
    suizaPlace = [
        "Lago Ginebra",
        "Matterhorn",
        "Interlaken",
        "Monte Titlis",
        "Zermatt",
        "Jungfraujoch",
        "Lago de Lucerna",
        "Rhine Falls",
        "Bern",
        "Zurich"
    ]
    if response.status_code == 200:
        print("   Ciudad       Coordenadas")
        for placeName, placeData in zip(suizaPlace, data['data']):
            latitude, longitude = placeData['latitude'], placeData['longitude']
            print(f"  {placeName}:   ({latitude}, {longitude})")
    else:
        print(f"Error: {response.status_code}")
else:
    print(f"Error: {response.status_code}")


