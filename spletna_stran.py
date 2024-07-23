import requests
import os

# url potresov
wiki_sez_potresov_url = "https://en.wikipedia.org/wiki/Lists_of_earthquakes"
# mapa, kjer je shranjena html datoteka
potresi_mapa = "podatki" 
# datoteka, kamor se shrani html stran
wiki_potresi_html = "wiki_stran.html"
# ime datoteke, kjer je shranjen csv
csv_dat_wiki = "wii_potresi.csv"

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

shrani_html(wiki_sez_potresov_url, potresi_mapa, wiki_potresi_html)








