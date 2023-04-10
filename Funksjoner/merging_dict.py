import requests
import beautifulsoup4 as bs4
from hentdata import hent_data
from hendatafrabolig import data_from_ads
from hentdatafravekst import vekstrate_funk


def merge_dict(dict1,dict2):

    for key1 in dict1.keys():
        bolignr = key1

    
    nummer = [int(s) for s in str.split(bolignr) if s.isdigit()][0]
    i = 1
    for key2 in dict2.keys():
        dict2["bolig "+str(nummer+i)] = dict2.pop(key2)
        i+=1

    return dict2


print(merge_dict(vekstrate_funk('https://www.finn.no/realestate/homes/search.html?location=2.20016.20318.20505&sort=PUBLISHED_DESC'),vekstrate_funk('https://www.finn.no/realestate/homes/search.html?location=1.20061.20520&sort=PUBLISHED_DESC')))