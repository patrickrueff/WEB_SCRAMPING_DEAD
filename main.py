import requests
from bs4 import BeautifulSoup
from time import sleep

# Listes des valeurs pour les variables
noms = ['Taffin', 'Durand']  # Vous pouvez ajouter d'autres noms ici
prenoms = ['Christine', 'Pierre']  # Vous pouvez ajouter d'autres prénoms ici
debut_dates = ['02/09/2005', '01/01/2007']  # Vous pouvez ajouter d'autres dates ici
fin_dates = ['01/09/2010', '01/01/2011']  # Vous pouvez ajouter d'autres dates ici

# Boucle à travers toutes les combinaisons de variables
for nom in noms:
    for prenom in prenoms:
        for debut in debut_dates:
            for fin in fin_dates:
                # Construire l'URL avec les paramètres actuels
                url = f"https://www.libramemoria.com/avis?nom={nom}&prenom={prenom}&debut={debut}&fin={fin}&departement=&commune=&communeName=&titre="

                
                
                #proxies = {
                # 'http': 'http://mon_proxy:8080',
                #     'https': 'http://mon_proxy:8080'
                #    }


                #response = requests.get(url, proxies=proxies)

                
                
                # Effectuer la requête HTTP GET
                response = requests.get(url)
                
                # Vérifier si la requête a réussi
                if response.status_code == 200:
                    # Analyser la page avec BeautifulSoup
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Extraire les avis de décès (vous devrez ajuster les sélecteurs en fonction de la structure HTML)
                    avis = soup.find_all('div', class_='obituary-item')  # Remplacez par le bon sélecteur CSS

                    # Afficher ou traiter chaque avis
                    for avis_item in avis:
                        nom_avis = avis_item.find('h2').text.strip()  # Ajustez selon la balise contenant le nom
                        date_avis = avis_item.find('time').text.strip()  # Ajustez selon la balise contenant la date
                        print(f'Nom: {nom_avis}, Date: {date_avis}')
                else:
                    print(f"Erreur lors de la requête pour {nom}, {prenom}, {debut} - {fin}: {response.status_code}")
                
                # Attendre quelques secondes entre les requêtes pour éviter de surcharger le serveur
                sleep(2)  # Ajustez ce délai si nécessaire
