def tempChargement(site):
    import requests
    import time

    debut = time.time()
    requests.get(site)
    temps= time.time() - debut
    return temps

def affiche(site,temps):
    print(f"Temps de chargement de {site} {temps}")


affiche("https://www.google.com/",tempChargement("https://www.google.com/"))
affiche("https://www.ynet.com/",tempChargement("https://www.ynet.com/"))
affiche("https://www.imdb.com/",tempChargement("https://www.imdb.com/"))

