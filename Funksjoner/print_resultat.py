import requests
import bs4
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

    print()
    
    faktisk_kapital = int(input('Hvor mange kroner har du tilgjengelig? '))

    #Utregning
    boligtall = []
    bolig_dict = vekstrate_funk()    #Endre til vekstrate
    for bolignr in bolig_dict:
        utregninger = verdi_utregning(bolig_dict[bolignr], faktisk_kapital)
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

            for bolig in range(len(boligliste)):
                eoc = boligliste[bolig][0]
                eoc_f = formating.f2(eoc)
                omlopsrate = boligliste[bolig][1]
                omlopsrate_f = formating.f2(omlopsrate)
                proi = boligliste[bolig][2]
                proi_f = formating.f0(proi)
                proi_f_p = formating.p(proi_f)
                endring_egenkapital = boligliste[bolig][3]
                endring_egenkapital_f = formating.f0(endring_egenkapital)
                endring_egenkapital_f_p = formating.p(endring_egenkapital_f)
                endring_egenkapital_prosent = boligliste[bolig][4]
                endring_egenkapital_prosent_f = formating.f2(endring_egenkapital_prosent)
                endring_egenkapital_prosent_per_aar = boligliste[bolig][5]
                endring_egenkapital_prosent_per_aar_f = formating.f2(endring_egenkapital_prosent_per_aar)
                lenke = boligliste[bolig][6]

                print(f'Bolig {bolig}   |   EOC: {eoc_f} - Omløpsrate: {omlopsrate_f} - PROI: {proi_f_p}   |   Fortjeneste: {endring_egenkapital_f_p} - Fortjeneste prosent: {endring_egenkapital_prosent_f} - Fortjeneste prosent per år: {endring_egenkapital_prosent_per_aar_f}  |   Lenke: {lenke}')


        #Relative tall      -       Sorterer etter "eoc"
        elif svar == 2:
            svar_test = True
            boligliste = sammenlign_relative_tall(boligtall)

            for bolig in range(len(boligliste)):
                eoc = boligliste[bolig][0]
                eoc_f = formating.f2(eoc)
                omlopsrate = boligliste[bolig][1]
                omlopsrate_f = formating.f2(omlopsrate)
                proi = boligliste[bolig][2]
                proi_f = formating.f2(proi)
                proi_f_p = formating.p(proi_f)
                lenke = boligliste[bolig][3]

                print(f'Bolig {bolig}   |   EOC: {eoc_f} - Omløpsrate: {omlopsrate_f} - PROI: {proi_f_p}    |   Lenke: {lenke}')
            

        #Eiendom            -       Sorterer etter "vekst_eiendomsverdi_prosent"
        elif svar == 3:
            svar_test = True
            boligliste = sammenlign_eiendom(boligtall)

            for bolig in range(len(boligliste)):
                eiendomsverdi = boligliste[bolig][0]
                eiendomsverdi_f = formating.f0(eiendomsverdi)
                eiendomsverdi_f_p = formating.p(eiendomsverdi_f)
                vekst_eiendomsverdi = boligliste[bolig][1]
                vekst_eiendomsverdi_f = formating.f0(vekst_eiendomsverdi)
                vekst_eiendomsverdi_f_p = formating.p(vekst_eiendomsverdi_f)
                vekst_eiendomsverdi_prosent = boligliste[bolig][2]
                vekst_eiendomsverdi_prosent_f = formating.f2(vekst_eiendomsverdi_prosent)
                vekst_eiendomsverdi_prosent_per_aar = boligliste[bolig][3]
                vekst_eiendomsverdi_prosent_per_aar_f = formating.f2(vekst_eiendomsverdi_prosent_per_aar)
                maanedlige_renter = boligliste[bolig][4]
                maanedlige_renter_f = formating.f0(maanedlige_renter)
                maanedlige_renter_f_p = formating.p(maanedlige_renter_f)
                total_renter_eiendom = boligliste[bolig][5]
                total_renter_eiendom_f = formating.f0(total_renter_eiendom)
                total_renter_eiendom_f_p = formating.p(total_renter_eiendom_f)
                lenke = boligliste[bolig][6]

                print(f'Bolig {bolig}   |   Kjøpsverdi: {eiendomsverdi_f_p}   |   Fortjeneste: {vekst_eiendomsverdi_f_p} - Fortjeneste prosent: {vekst_eiendomsverdi_prosent_f} - Fortjeneste prosent per år: {vekst_eiendomsverdi_prosent_per_aar_f}   |   Maanedlige renter: {maanedlige_renter_f_p} - Totale renter: {total_renter_eiendom_f_p}  |   Lenke: {lenke}')


        #Leietall           -       Sorterer etter "tilbakebetalt_laan"
        elif svar == 4:
            svar_test = True
            boligliste = sammenlign_leie(boligtall)

            for bolig in range(len(boligliste)):
                tilbakebetalt_laan = boligliste[bolig][0]
                tilbakebetalt_laan_f = formating.f0(tilbakebetalt_laan)
                tilbakebetalt_laan_f_p = formating.p(tilbakebetalt_laan_f)
                ny_laanesum = boligliste[bolig][1]
                ny_laanesum_f = formating.f0(ny_laanesum)
                ny_laanesum_f_p = formating.p(ny_laanesum_f)
                total_renter_leie = boligliste[bolig][2]
                total_renter_leie_f = formating.f0(total_renter_leie)
                total_renter_leie_f_p = formating.p(total_renter_leie_f)
                lenke = boligliste[bolig][3]

                print(f'Bolig {bolig}   |   Tilbakebetalt lån: {tilbakebetalt_laan_f_p} - Ny lånesum: {ny_laanesum_f_p}   |   Totale renter: {total_renter_leie_f_p}    |   Lenke: {lenke}')


        else:
            print('Ikke et gyldig valg.')
