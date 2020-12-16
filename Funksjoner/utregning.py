# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:36:32 2020

@author: henri
"""

def renter_utregning (lånesum):
    #Regne renter
    rentesats = 1.5 #Henter beste fra nettside med oversikt
    renter = lånesum * rentesats
    
    return renter


def verdi_utregning (liste):   #Liste = [Prisantydning, Kvadratmeterpris, Størrelse, Område, [Felleskostnad, Kommunale avgifter, Strøm/Varme, Internett], Antall Soverom]
    #Regne verdi eiendom
    
    
    
    #Regne verdi leie
    
    #Konstanter
    måneder = 12
    leieinntekt = 5700
    egenkapital = 0.15
    
    #Variabler
    lånesum = liste[0] * (1 - egenkapital)
    kvmpris = liste[1]
    størrelse = liste[2]
    område = liste[3]
    leietagere = liste[5] - 1
    
    felleskost = liste[4][0]
    kommunalavgift = liste[4][1]
    strøm = liste[4][2]
    internett = liste[4][3]
    
    #Kostnader
    kostnader = felleskost + kommunalavgift + strøm + internett
    
    for år in range(10):
        for måned in range(12):
            renter = renter_utregning(lånesum)
    
    
    #Inntekter
    
    
    
    
    
    
    
    