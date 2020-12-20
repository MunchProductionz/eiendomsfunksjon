# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:36:32 2020

@author: henri
"""
#################
#Mulie parametere
#################

## Prisantydning
# Kvadratmeterpris
# Størrelse
# Område
# Felleskostnad, Kommunale avgifter, Strøm/Varme, Internett, KabelTV
## Antall Soverom

# Input tilgjengelig kapital


def verdi_utregning (liste):   #Liste = [Prisantydning, Kvadratmeterpris, Størrelse, Område, [Felleskostnad, Kommunale avgifter, Strøm/Varme, Internett], Antall Soverom]
    
    #Konstanter
    måneder = 12    
    år = 10
    total_måneder = måneder * år
    leieinntekt = 5700
    egenkapital = 0.15
    r = 1.02                #Hente rentesats fra bank/nettside
    rentesum = r**år
    forventet_vekst = 1.1   #Hente ved bruk av område-variabel
    
    #Variabler fra liste
    eiendomspris = liste[0]
    lånesum = eiendomspris * (1 - egenkapital)
    kvmpris = liste[1]
    størrelse = liste[2]
    område = liste[3]
    leietagere = liste[5] - 1
    
    felleskost = liste[4][0]
    kommunalavgift = liste[4][1]
    strøm = liste[4][2]
    internett = liste[4][3]
    

    ####################
    #Regne verdi eiendom
    ####################

    #Eiendomsverdi / Månedlige renter
    vekst_eiendomsverdi = vekst_rek_år(eiendomspris, år, forventet_vekst)
    eiendomsverdi = eiendomspris + vekst_eiendomsverdi
    
    #Renter boliglån
    årlige_renter = lånesum * r
    månedlige_renter = årlig_renter / måneder
    total_renter_eiendom = årlige_renter * år

    #Endring egenkapital
    endring_egenkapital = eiendomsverdi - eiendomspris - total_renter_eiendom

    eiendom = list(endring_egenkapital, eiendomsverdi, vekst_eiendomsverdi, månedlige renter, total_renter)


    #################
    #Regne verdi leie
    #################

    #        #
    #Inntekter
    #        #

    månedlig_inntekt_u = leietagere * leieinntekt
    månedlig_inntekt_m = månedlig_inntekt_u + leieinntekt           #Betale "leieinntekt" fra egen lomme
    årlig_inntekt_u = månedlig_inntekt_u * måneder
    årlig_inntekt_m = månedlig_inntekt_m * måneder                  


    #        #
    #Kostnader
    #        #
    
    #Faste avgifter - Leie
    månedlige_felleskostnader = felleskost + kommunalavgift + strøm + internett
    eierleie = leieinntekt
    månedlige_eierkostnader = (månedlige_felleskostnader / (leietagere + 1)) + eierleie

    #Renter / Avdrag - Leie
    totale_renter_leie = renter_rek_mån(lånesum, månedlig_inntekt_m, total_måneder, r)

    #Lånesum etter x antall år
    ny_lånesum = lånesum - totale_renter_leie

    #Tilbakebetalt lån
    tilbakebetalt_lån = tilbakebetalt_rek_mån(lånesum, månedlig_inntekt_m, total_måneder, r)

    leie = list(tilbakebetalt_lån, ny_lånesum, månedlige_eierkostnader, totale_renter_leie)


    ###############
    #Return verdier
    ###############
    
    #listeliste = [endring_egenkapital, eiendomsverdi, vekst eiendomsverdi, månedlige renter, total_renter, tilbakebetalt_lån, ny_lånesum, månedlige_eierkostnader, totale_renter_leie]
    listeliste = eiendom + leie

    return listeliste
    
    
    