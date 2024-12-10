import requests
from dotenv import load_dotenv
import os

load_dotenv(override=True)
MY_API_KEY = os.getenv("MY_API_KEY")

def call_api(endpoint, method="GET", data=None):
    base_url = "http://engtec.pythonanywhere.com"  # Substitua pelo URL base da sua API
    headers = {"Content-Type": "application/json","authorization":f"Bearer {MY_API_KEY}"}
    try:
        if method == "GET":
            response = requests.get(f"{base_url}{endpoint}", headers=headers)
        elif method == "POST":
            response = requests.post(f"{base_url}{endpoint}", headers=headers, json=data)
        elif method == "PUT":
            response = requests.put(f"{base_url}{endpoint}", headers=headers, json=data)
        elif method == "PATCH":
            response = requests.patch(f"{base_url}{endpoint}", headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(f"{base_url}{endpoint}", headers=headers, json=data)
        else:
            return {"error": "Método HTTP inválido"}
        
        return response.json()
    except Exception as e:
        return {"error": str(e)}
