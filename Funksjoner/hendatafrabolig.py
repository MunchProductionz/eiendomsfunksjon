import requests
import bs4
from hentdata import hent_data



soup = hent_data('https://www.finn.no/realestate/homes/search.html?location=2.20016.20318.20505&sort=PUBLISHED_DESC')



def annonse_lenke(soup):
    ad_links = []
    for link in soup.find_all('a',{"class":"ads__unit__link"}):
        ad_links.append(link['href'])
    
    return ad_links


def data_from_ads():
    ad_links = annonse_lenke(soup)
    bolig_dict = {}
    for lenke, count in enumerate(ad_links):
        ad_soup = hent_data(lenke)
        prisantydning = ad_soup.select('u-t3').text
        bolig_dict.setdefault("bolig%a"%(count),prisantydning)

    
    return bolig_dict

print(data_from_ads())



            


