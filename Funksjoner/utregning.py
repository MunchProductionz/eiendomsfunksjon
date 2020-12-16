# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:36:32 2020

@author: henri
"""


def verdi_utregning (liste):   #Liste = [Prisantydning, Kvadratmeterpris, Størrelse, Område, [Felleskostnad, Kommunale avgifter, Strøm/Varme, Internett], Antall Soverom]
    #Regne verdi eiendom
    
    
    
    #Regne verdi leie
    
    #Konstanter
    måneder = 12
    år = 10
    leieinntekt = 5700
    egenkapital = 0.15
    r = 1.02                #Hente rentesats fra bank/nettside
    rentesum = r**år
    
    #Variabler fra liste
    lånesum = liste[0] * (1 - egenkapital)
    kvmpris = liste[1]
    størrelse = liste[2]
    område = liste[3]
    leietagere = liste[5] - 1
    
    felleskost = liste[4][0]
    kommunalavgift = liste[4][1]
    strøm = liste[4][2]
    internett = liste[4][3]
    
    ####Inntekter
    



    ####Kostnader
    
    #Faste avgifter
    kostnader = felleskost + kommunalavgift + strøm + internett

    #Renter / Avdrag
    renter = renter_test(lånesum, rentesats)

    årlig_inntekt = inntekter / år
    renter = renter_rek(lånesum, årlig_inntekt, år, r)




    
    
    
    
    
    
    