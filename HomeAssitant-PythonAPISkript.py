import requests


HASS_URL = "http://192.168.178.65:8123/api/services/switch/toggle"                          
TOKEN = "12345"

data = {          
    "entity_id": "switch.fernseher" # oder auch light.licht 
}


headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

response = requests.post(HASS_URL, headers=headers, json=data)

if response.status_code == 200:
    print("Erfolgreich ausgeführt!")
else:
    print(f"Fehler: {response.status_code}")
