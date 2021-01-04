import requests
import bs4
from hentdata import hent_data







def annonse_lenke(soup):
    ad_links = []
    for link in soup.find_all('a',{"class":"ads__unit__link"}):
        
        ad_links.append(link['href'])
        
    return ad_links


def data_from_ads(finn_lenke):

    soup = hent_data(finn_lenke)
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


    
        postnummer_adresse = ad_soup.find("p",{"class": "u-caption"}).get_text()

        def reverse_string(string):
            return string[::-1]
        s = [int(s) for s in str.split(reverse_string(postnummer_adresse)) if s.isdigit()]
        
        postnummer = reverse_string(str(s[0]))
        
        if len(postnummer) == 3:
            postnummer = int(postnummer)*10
            bolig_info.append(str(postnummer))
        else:
            bolig_info.append(postnummer)


        for pris in ad_soup.select('span.u-t3:contains("kr")'):
            prisantydning = (pris.text).replace(" ","").strip()
            bolig_info.append(prisantydning)

        bolig_info.append(lenke)
        bolig_dict.setdefault(bolignr,bolig_info)
    
    return bolig_dict
      
       



#Output

#Dictionary['Bolig 1'] = [Fylke, By, Prisantydning, Lenke]




            




            


