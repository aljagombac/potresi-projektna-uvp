import requests
import os
import re

# url potresov
wiki_potres_url = "https://en.wikipedia.org/wiki/List_of_earthquakes_in_2024"
# mapa, kjer je shranjena html datoteka
potresi_mapa = "podatki" 
# datoteka, kamor se shrani html stran
wiki_potres_html = "wiki_stran.html"
# ime datoteke, kjer je shranjen csv
csv_dat_wiki = "wiki_potresi.csv"

def shrani_url_v_niz(url):
    """Vrne vsebino strani kot niz."""
    try:
        stran = requests.get(url)        
        vsebina = stran.text
        return vsebina
    except requests.exceptions.RequestException:
        # koda, ki se izvede če pride do napake
        print("Prišlo je do napake pri nalaganju vsebine!")
        return None
    
def shrani_niz_v_datoteko(text, mapa, datoteka):
    """Zapiše niz v novo ustvarjeno datoteko."""
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, datoteka)
    with open(pot, 'w', encoding='utf-8') as dat:
        dat.write(text)
    return None

def shrani_html(url, mapa, datoteka):
    '''Shrani niz url-ja v html datoteko.'''
    text = shrani_url_v_niz(url)
    shrani_niz_v_datoteko(text, mapa, datoteka)

#shrani nize urlj-ev potresov za leta 2010-2024 v html datoteke
for n in range(2010, 2025):
    wiki_html = f"wiki_potres_{n}.html"
    if n == 2024:
      shrani_html(wiki_url, potresi_mapa, wiki_html)
    else:    
        wiki_url = wiki_potres_url.replace("2024", str(n))
        shrani_html(wiki_url, potresi_mapa, wiki_html) 








