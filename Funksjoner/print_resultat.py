import requests
import bs4
import re
import hentdata
import hentdatafrabolig
import hjelpefunksjoner
import vekstfunksjoner
import utregning
import sammenligning
import print_resultat

#Muligheter
# Sammenligne relevante tall utenom leie    -   sammenlign_relevante_tall_ul(verdi_utregning(boligdata))
# Sammenligne relative tall                 -   sammenlign_relative_tall(verdi_utregning(boligdata))
# Sammenligne eiendomstall                  -   sammenlign_eiendom(verdi_utregning(boligdata))
# Sammenligne leietall                      -   sammenlign_leie(verdi_utregning(boligdata))


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
    for bolignr in bolig_dict:
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
                total_renter_leie = boligliste[bolig][2]
                lenke = boligliste[bolig][3]

                print(f'Bolig {bolig}   |   Tilbakebetalt lån: {tilbakebetalt_laan} - Ny lånesum: {ny_laanesum}   |   Totale renter: {total_renter_leie}   |   Lenke: {lenke}')


        else:
            print('Ikke et gyldig valg.')
