import requests
import bs4
import re

# Complete program



# Hent data
def hent_data(link):

    res = requests.get(link)

    
    soup = bs4.BeautifulSoup(res.text,'lxml')


    return soup


soup = hent_data('https://www.finn.no/realestate/homes/search.html?location=2.20016.20318.20505&sort=PUBLISHED_DESC')


# Hent lenke
def annonse_lenke(soup):
    ad_links = []
    for link in soup.find_all('a',{"class":"ads__unit__link"}):
        
        ad_links.append(link['href'])
        
    return ad_links


# Hent data
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
      

# Hjelpefunksjoner
def takeFirst (list):
    return list[0]
def takeSecond (list):
    return list[1]


# Vekstfunksjoner
def renter_test (laanesum, rentesats):
    return laanesum * rentesats
def renter_rek_maan (laanesum, maanedlig_inntekt_m, total_maaneder, r):
    renter = (laanesum * (r - 1)) / 12                       #Regner renter
    ny_laanesum = (laanesum + renter) - maanedlig_inntekt_m    #Regner ny laanesum
    total_maaneder -= 1                                      #Trekker fra 1 maaned fra total

    if total_maaneder == 1:                                  #Sluttbetingelse
        return renter
    else:                                                   #Kaller seg selv med ny laanesum som parameter
        return renter + renter_rek_maan(ny_laanesum, maanedlig_inntekt_m, total_maaneder, r)
def tilbakebetalt_rek_maan (laanesum, maanedlig_inntekt_m, total_maaneder, r):
    renter = (laanesum * (r - 1)) / 12                       #Regner renter
    ny_laanesum = (laanesum + renter) - maanedlig_inntekt_m    #Regner ny laanesum
    tilbakebetalt_sum = laanesum - ny_laanesum
    total_maaneder -= 1                                      #Trekker fra 1 maaned fra total

    if total_maaneder == 1:                                  #Sluttbetingelse
        return tilbakebetalt_sum
    else:                                                   #Kaller seg selv med ny laanesum som parameter
        return tilbakebetalt_sum + tilbakebetalt_rek_maan(ny_laanesum, maanedlig_inntekt_m, total_maaneder, r)
def vekst_rek_aar (verdi, aar, veksttall):
    vekst = verdi * veksttall
    ny_verdi = verdi + vekst
    aar -= 1

    if aar == 1:
        return vekst
    else:
        return vekst + vekst_rek_aar(ny_verdi, aar, veksttall)


# Utregning
def verdi_utregning (liste):
    
    #Konstanter
    maaneder = 12    
    aar = 10                #Input
    total_maaneder = maaneder * aar
    egenkapital = 0.15
    r = 1.02                #Hente rentesats fra bank/nettside
    rentesum = r**aar
    forventet_vekst = 1.1   #Hente ved bruk av omraade-variabel
    leieinntekt = 5700      #Hente
    leietagere = 2          #Hente
    
    #Variabler fra liste
    omraade = liste[0]
    eiendomspris = liste[2]
    lenke = liste[3]
    laanesum = eiendomspris * (1 - egenkapital)

    

    ####################
    #Regne verdi eiendom
    ####################

    #Vekst eiendomsverdi
    vekst_eiendomsverdi = vekst_rek_aar(eiendomspris, aar, forventet_vekst)
    vekst_eiendomsverdi_prosent = vekst_eiendomsverdi / eiendomspris
    vekst_eiendomsverdi_prosent_per_aar = vekst_eiendomsverdi_prosent / aar
    
    #Eiendomsverdi
    eiendomsverdi = eiendomspris + vekst_eiendomsverdi
    
    #Renter boliglaan
    maanedlige_renter = aar/ maaneder
    aarlige_renter = laanesum * r
    total_renter_eiendom = aarlige_renter * aar

    #Endring egenkapital
    endring_egenkapital = eiendomsverdi - eiendomspris - total_renter_eiendom
    endring_egenkapital_prosent = endring_egenkapital / egenkapital
    endring_egenkapital_prosent_per_aar = endring_egenkapital_prosent / aar

    #Faktisk egenkapital
    faktisk_egenkapital = input('Hvor mange kroner har du tilgjengelig? ')
    potenisell_laanesum = faktisk_egenkapital / egenkapital

    #Gevinst mot innsats (Efficieny of Capital)
    eoc = endring_egenkapital_prosent * (laanesum / potenisell_laanesum) * 100  #100 gjor bare tallene penere

    #Omlopsrate 
    omlopsrate = potenisell_laanesum / laanesum

    #Maksimal potensiell endring egenkapital (Potential Returns on Investment)
    proi = endring_egenkapital_prosent * omlopsrate


    relative_tall = list(eoc, omlopsrate, proi)
    egenkapital = list(endring_egenkapital, endring_egenkapital_prosent, endring_egenkapital_prosent_per_aar)
    eiendom = list(eiendomsverdi, vekst_eiendomsverdi, vekst_eiendomsverdi_prosent, vekst_eiendomsverdi_prosent_per_aar, maanedlige_renter, total_renter_eiendom)



    #################
    #Regne verdi leie
    #################

    #        #
    #Inntekter
    #        #

    eierleie = leieinntekt
    maanedlig_inntekt_u = leietagere * leieinntekt
    maanedlig_inntekt_m = maanedlig_inntekt_u + leieinntekt           #Betale "eierleie" fra egen lomme
    aarlig_inntekt_u = maanedlig_inntekt_u * maaneder
    aarlig_inntekt_m = maanedlig_inntekt_m * maaneder                  


    #        #
    #Kostnader
    #        #
    
    #Faste avgifter - Leie
    #maanedlige_felleskostnader = felleskost + kommunalavgift + strom + internett
    #maanedlige_eierkostnader = (maanedlige_felleskostnader / (leietagere + 1)) + eierleie

    #Renter / Avdrag - Leie
    total_renter_leie = renter_rek_maan(laanesum, maanedlig_inntekt_m, total_maaneder, r)

    #Tilbakebetalt laan
    tilbakebetalt_laan = tilbakebetalt_rek_maan(laanesum, maanedlig_inntekt_m, total_maaneder, r)
    ny_laanesum = laanesum - tilbakebetalt_laan

    leie = list(tilbakebetalt_laan, ny_laanesum, maanedlige_eierkostnader, totale_renter_leie)


    ###############
    #Return verdier
    ###############

    #listeliste = []
    listeliste = []
    listeliste.append(relative_tall)
    listeliste.append(egenkapital)
    listeliste.append(eiendom)
    listeliste.append(leie)
    listeliste.append(lenke)

    return listeliste


# Sammenligning
def sammenlign_relevante_tall_ul (listeliste):

    ##########
    #Variabler
    ##########

    #eoc = listeliste[i][0][0]
    #omlopsrate = listeliste[i][0][1]
    #proi = listeliste[i][0][2]

    #endring_egenkapital = listeliste[i][1][0]
    #endring_egenkapital_prosent = listeliste[i][1][1]
    #endring_egenkapital_prosent_per_aar = listeliste[i][1][2]
    #lenke = listeliste[i][4][0]
    relevante_tall_ul = []


    ###################
    #Sortere etter eoc#
    ###################

    for liste in listeliste:
            eoc = liste[0][0]
            omlopsrate = liste[0][1]
            proi = liste[0][2]
            endring_egenkapital = liste[1][0]
            endring_egenkapital_prosent = liste[1][1]
            endring_egenkapital_prosent_per_aar = liste[1][2]
            lenke = liste[4][0]

            relevante_tall_ul.append(eoc)
            relevante_tall_ul.append(omlopsrate)
            relevante_tall_ul.append(proi)
            relevante_tall_ul.append(endring_egenkapital)
            relevante_tall_ul.append(endring_egenkapital_prosent)
            relevante_tall_ul.append(endring_egenkapital_prosent_per_aar)
            relevante_tall_ul.append(lenke)

    relevante_tall_ul = sorted(relevante_tall_ul, key=lambda l:l[0], reverse = False)
                                                
    return relevante_tall_ul
def sammenlign_relative_tall (listeliste):

    ##########
    #Variabler
    ##########

    #eoc = listeliste[i][1][0]
    #omlopsrate = listeliste[i][1][1]
    #proi = listeliste[i][1][2]
    #lenke = listeliste[i][4][0]
    relative_tall = []


    ###################
    #Sortere etter poc#
    ###################

    for liste in listeliste:
        eoc = liste[0][0]
        omlopsrate = liste[0][1]
        proi = liste[0][2]
        lenke = liste[4][0]

        relative_tall.append(eoc)
        relative_tall.append(omlopsrate)
        relative_tall.append(proi)
        relative_tall.append(lenke)

    relative_tall = sorted(relative_tall, key=lambda l:l[0], reverse = False)
            
    return relative_tall
def sammenlign_eiendom (listeliste):

    ##########
    #Variabler
    ##########

    #eiendomsverdi = listeliste[i][2][0]
    #vekst_eiendomsverdi = listeliste[i][2][1]
    #vekst_eiendomsverdi_prosent = listeliste[i][2][2]
    #vekst_eiendomsverdi_prosent_per_aar = listeliste[i][2][3]
    #maanedlige_renter = listeliste[i][2][4]
    #total_renter_eiendom = listeliste[i][2][5]
    #lenke = listeliste[i][4][0]
    eiendomstall = []


    #####################################
    #Sortere etter vekst_eiendomsverdi_prosent#
    #####################################

    for liste in listeliste:
        eiendomsverdi = liste[2][0]
        vekst_eiendomsverdi = liste[2][1]
        vekst_eiendomsverdi_prosent = liste[2][2]
        vekst_eiendomsverdi_prosent_per_aar = liste[2][3]
        maanedlige_renter = liste[2][4]
        total_renter_eiendom = liste[2][5]
        lenke = liste[4][0]

        eiendomstall.append(eiendomsverdi)
        eiendomstall.append(vekst_eiendomsverdi)
        eiendomstall.append(vekst_eiendomsverdi_prosent)
        eiendomstall.append(vekst_eiendomsverdi_prosent_per_aar)
        eiendomstall.append(maanedlige_renter)
        eiendomstall.append(total_renter_eiendom)
        eiendomstall.append(lenke)

    eiendomstall = sorted(eiendomstall, key=lambda l:l[2], reverse = False)
                                            
    return eiendomstall
def sammenlign_leie (listeliste):

    ##########
    #Variabler
    ##########

    #tilbakebetalt_laan = listeliste[i][3][0]
    #ny_laanesum = listeliste[i][3][1]
    #maanedlige_eierkostnader = listeliste[i][3][2]
    #total_renter_leie = listeliste[i][3][3]
    #lenke = listeliste[i][4][0]
    leietall = []


    #################################
    #Sortere etter tilbakebetalt_laan#
    #################################

    for liste in listeliste:
        tilbakebetalt_laan = liste[3][0]
        ny_laanesum = liste[3][1]
        maanedlige_eierkostnader = liste[3][2]
        total_renter_leie = liste[3][3]
        lenke = liste[4][0]

        leietall.append(tilbakebetalt_laan)
        leietall.append(ny_laanesum)
        leietall.append(maanedlige_eierkostnader)
        leietall.append(total_renter_leie)
        leietall.append(lenke)

    leietall = sorted(leietall, key=lambda l:l[0], reverse = False)

    return leietall


# Print resultat
def print_resultat ():

    #Input
    print('Programmet sammenligner ulikt basert på ulik output.')
    print()
    print(' 1. Relevante tall utenom leie')
    print(' 2. Relative tall')
    print(' 3. Eiendomstall')
    print(' 4. Leietall')

    svar = int(input('Skriv inn tallet til ønsket output: '))


    #Utregning
    boligtall = []
    bolig_dict = data_from_ads()
    for bolignr in bolig_dict
        utregninger = verdi_utregning(bolig_dict[bolignr])
        boligtall.append(utregninger)


    ###############
    #Sammenligning#
    ###############

    svar_test = False

    while svar_test == False:

        #Relevante tall     -       Sorterer etter "eoc"
        if svar == 1:
            svar_test = True
            boligliste = sammenlign_relevante_tall_ul(boligtall)

            for bolig in range(boligliste):
                eoc = boligliste[bolig][0]
                omlopsrate = boligliste[bolig][1]
                proi = boligliste[bolig][2]
                endring_egenkapital = boligliste[bolig][3]
                endring_egenkapital_prosent = boligliste[bolig][4]
                endring_egenkapital_prosent_per_aar = boligliste[bolig][5]
                lenke = boligliste[bolig][6]

                print(f'Bolig {bolig}   |   EOC: {eoc} - Omløpsrate: {omlopsrate} - PROI: {proi}   |   Fortjeneste: {endring_egenkapital} - Fortjeneste prosent: {endring_egenkapital_prosent} - Fortjeneste prosent per år: {endring_egenkapital_prosent_per_aar}   |   Lenke: {lenke}')


        #Relative tall      -       Sorterer etter "eoc"
        elif svar == 2:
            svar_test = True
            boligliste = sammenlign_relative_tall(boligtall)

            for bolig in range(boligliste):
                eoc = boligliste[bolig][0]
                omlopsrate = boligliste[bolig][1]
                proi = boligliste[bolig][2]
                lenke = boligliste[bolig][3]

                print(f'Bolig {bolig}   |   EOC: {eoc} - Omløpsrate: {omlopsrate} - PROI: {proi}   |   Lenke: {lenke}')
            

        #Eiendom            -       Sorterer etter "vekst_eiendomsverdi_prosent"
        elif svar == 3:
            svar_test = True
            boligliste = sammenlign_eiendom(boligtall)

            for bolig in range(boligliste):
                eiendomsverdi = boligliste[bolig][0]
                vekst_eiendomsverdi = boligliste[bolig][1]
                vekst_eiendomsverdi_prosent = boligliste[bolig][2]
                vekst_eiendomsverdi_prosent_per_aar = boligliste[bolig][3]
                maanedlige_renter = boligliste[bolig][4]
                total_renter_eiendom = boligliste[bolig][5]
                lenke = boligliste[bolig][6]

                print(f'Bolig {bolig}   |   Kjøpsverdi: {eiendomsverdi}   |   Fortjeneste: {vekst_eiendomsverdi} - Fortjeneste prosent: {vekst_eiendomsverdi_prosent} - Fortjeneste prosent per år: {vekst_eiendomsverdi_prosent_per_aar}   |   Maanedlige renter: {maanedlige_renter} - Totale renter: {total_renter_eiendom}   |   Lenke: {lenke}')


        #Leietall           -       Sorterer etter "tilbakebetalt_laan"
        elif svar == 4:
            svar_test = True
            boligliste = sammenlign_leie(boligtall)

            for bolig in range(boligliste):
                tilbakebetalt_laan = boligliste[bolig][0]
                ny_laanesum = boligliste[bolig][1]
                maanedlige_eierkostnader = boligliste[bolig][2]
                total_renter_leie = boligliste[bolig][3]
                lenke = boligliste[bolig][4]

                print(f'Bolig {bolig}   |   Tilbakebetalt lån: {tilbakebetalt_laan} - Ny lånesum: {ny_laanesum}   |   Månedlige eierkostnader: {maanedlige_eierkostnader} - Totale renter: {total_renter_leie}   |   Lenke: {lenke}')


        else:
            print('Ikke et gyldig valg.')


# Main
def main ():
    print_resultat()

main()