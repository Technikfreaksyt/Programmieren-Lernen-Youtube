import requests

# Home Assistant Einstellungen
HASS_URL = "http://IP_ADRESSE:8123/api/services/switch/toggle" # oder auch /light/toggle, usw    
TOKEN = "API Token von Home Assistant"

# Service-Daten (zum Beispiel, um eine Licht zu schalten)
data = {
    "entity_id": "switch.template" # oder auch light.licht 
}

# HTTP-Anfrage an Home Assistant senden
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

response = requests.post(HASS_URL, headers=headers, json=data)

if response.status_code == 200:
    print("Erfolgreich ausgeführt!")
else:
    print(f"Fehler: {response.status_code}")
