import requests

# Tester la connexion à Google
try:
    response = requests.get("https://www.google.com")
    print("Connexion à Google réussie", response.status_code)
except requests.ConnectionError:
    print("Échec de la connexion à Google")

# Tester la connexion à libramemoria
try:
    response = requests.get("https://www.libramemoria.com")
    print("Connexion à Libramemoria réussie", response.status_code)
except requests.ConnectionError:
    print("Échec de la connexion à Libramemoria")
