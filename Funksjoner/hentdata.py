import requests
import bs4

def hent_data(link):

    res = requests.get(link)


    soup = bs4.BeautifulSoup(res.text,'lxml')


    return soup


