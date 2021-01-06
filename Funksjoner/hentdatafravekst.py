import requests
import bs4
from hentdata import hent_data
from hendatafrabolig import data_from_ads



def postnummer_side(postnummer):
    soup = hent_data('https://www.krogsveen.no/prisstatistikk?zipCode='+ postnummer)

    return soup



def vekstrate_funk(finn_lenke):
    bolig_dict = data_from_ads(finn_lenke)
    for key, items in bolig_dict.items():
        postnr = items[2]
        soup = postnummer_side(postnr)
        vekstrate = soup.find("h1",{"class":"css-10rlvwe"}).get_text()
        bolig_dict[key].insert(4,vekstrate)
    return bolig_dict

#print(vekstrate_funk('https://www.finn.no/realestate/homes/search.html?location=2.20016.20318.20505&sort=PUBLISHED_DESC'))


