import requests
import certifi
from bs4 import BeautifulSoup

# URL de la page de connexion
login_url = 'https://www.protys.fr/login'

# Dictionnaire des informations de connexion (remplacer par vos vraies informations)
login_payload = {
    'email': 'patrick.rueff@suez.com',  # Remplacez par votre email
    'password': 'Marion01',    # Remplacez par votre mot de passe
}

# Créer une session pour maintenir la connexion
with requests.Session() as session:
    # Utiliser le bundle de certificats fourni par certifi
    login_page = session.get(login_url, verify=certifi.where())
    
    # Soumettre le formulaire de connexion
    login_response = session.post(login_url, data=login_payload, verify=certifi.where())
    
    # Vérifier si la connexion a réussi
    if login_response.status_code == 200:
        print("Connexion réussie")
        
        # Accéder à la page post-connexion
        post_login_page = session.get('https://www.protys.fr/page_apres_connexion', verify=certifi.where())
        soup = BeautifulSoup(post_login_page.text, 'html.parser')
        print(soup.prettify())
    else:
        print(f"Échec de la connexion, statut: {login_response.status_code}")
