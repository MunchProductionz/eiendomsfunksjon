import requests
import beautifulsoup4 as bs4
from hentdata import hent_data




def hent_rente(bolig_side):
    laanebelop = (input("Tast inn lånebløpet ditt: "))
    nedbetalingaar = int(("Tast inn nedbetalingsaar: "))

    soup = hent_data("https://www.smartepenger.no/markedsoversikter/1026-boliglanskalkulator")
    


