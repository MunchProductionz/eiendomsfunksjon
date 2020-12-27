import requests
import bs4
import re
from hentdata import hent_data



soup = hent_data('https://www.finn.no/realestate/homes/search.html?location=2.20016.20318.20505&sort=PUBLISHED_DESC')



def annonse_lenke(soup):
    ad_links = []
    for link in soup.find_all('a',{"class":"ads__unit__link"}):
        
        ad_links.append(link['href'])
        
    return ad_links


def data_from_ads():
    ad_links = annonse_lenke(soup)
    del(ad_links[0])
    bolig_dict = {}
    for count, lenke in enumerate(ad_links, start=1):
        ad_soup = hent_data(lenke)
        bolignr = "bolig"+str(count)
        bolig_info = []

        for checkbox in soup.find_all('input', checked=True,limit=2):
            omraade_1 = checkbox.find_next_sibling("label").get_text()
            omraade = ''.join([i for i in omraade_1 if not i.isdigit()])
            omraade = omraade.replace("(","")
            omraade = omraade.replace(")","")
            bolig_info.append(omraade)


        

        for pris in ad_soup.select('span.u-t3:contains("kr")'):
            prisantydning = (pris.text).replace(" ","").strip()
            bolig_info.append(prisantydning)

        bolig_dict.setdefault(bolignr,bolig_info)
    
    return bolig_dict
      
       

print(data_from_ads())






            




            


