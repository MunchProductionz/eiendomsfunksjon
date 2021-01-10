#################
#Mulie parametere
#################

## Prisantydning
# Kvadratmeterpris
# Storrelse
# Omraade
# Felleskostnad, Kommunale avgifter, Strom/Varme, Internett, KabelTV
## Antall Soverom

#bolig_dict = {'Bolig 1' = [Fylke, By, Prisantydning, Lenke], ...}
#liste = [Fylke, By, Postnummer, Prisantydning, Vekstrate, Lenke]

# Input tilgjengelig kapital


def verdi_utregning (liste, faktisk_kapital):
    
    #Konstanter
    maaneder = 12    
    aar = 10
    total_maaneder = maaneder * aar
    egenkapital = 0.15
    r = 1.02                #Hente rentesats fra bank/nettside
    rentesum = r**aar
    leieinntekt = 5700
    leietagere = 2
    
    #Variabler fra liste
    #omraade = liste[0]
    eiendomspris = hjelpefunksjoner.removesoup(liste[2])
    forventet_vekst = hjelpefunksjoner.removesoup(liste[4])
    lenke = liste[5]
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
    aarlige_renter = laanesum * r
    maanedlige_renter = aarlige_renter / maaneder
    total_renter_eiendom = aarlige_renter * aar

    #Endring egenkapital
    endring_egenkapital = eiendomsverdi - eiendomspris - total_renter_eiendom
    endring_egenkapital_prosent = endring_egenkapital / egenkapital
    endring_egenkapital_prosent_per_aar = endring_egenkapital_prosent / aar

    #Faktisk egenkapital
    faktisk_egenkapital = faktisk_kapital
    potenisell_laanesum = faktisk_egenkapital / egenkapital

    #Gevinst mot innsats (Efficieny of Capital)
    eoc = endring_egenkapital_prosent * (laanesum / potenisell_laanesum) * 100  #100 gjor bare tallene penere

    #Omlopsrate 
    omlopsrate = potenisell_laanesum / laanesum

    #Maksimal potensiell endring egenkapital (Potential Returns on Investment)
    proi = endring_egenkapital_prosent * omlopsrate


    relative_tall = [eoc, omlopsrate, proi]
    egenkapital = [endring_egenkapital, endring_egenkapital_prosent, endring_egenkapital_prosent_per_aar]
    eiendom = [eiendomsverdi, vekst_eiendomsverdi, vekst_eiendomsverdi_prosent, vekst_eiendomsverdi_prosent_per_aar, maanedlige_renter, total_renter_eiendom]



    #################
    #Regne verdi leie
    #################

    #        #
    #Inntekter
    #        #

    #eierleie = leieinntekt
    maanedlig_inntekt_u = leietagere * leieinntekt
    maanedlig_inntekt_m = maanedlig_inntekt_u + leieinntekt           #Betale "eierleie" fra egen lomme
    #aarlig_inntekt_u = maanedlig_inntekt_u * maaneder
    #aarlig_inntekt_m = maanedlig_inntekt_m * maaneder                  


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

    leie = [tilbakebetalt_laan, ny_laanesum, total_renter_leie]


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
    
    
    