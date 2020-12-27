#Muligheter
# Sammenligne relevante tall utenom leie    -   sammenlign_relevante_tall_ul(verdi_utregning(boligdata))
# Sammenligne relative tall                 -   sammenlign_relative_tall(verdi_utregning(boligdata))
# Sammenligne eiendomstall                  -   sammenlign_eiendom(verdi_utregning(boligdata))
# Sammenligne leietall                      -   sammenlign_leie(verdi_utregning(boligdata))


def print ():

    #Input
    print('Programmet sammenligner ulikt basert på ulik output.')
    print()
    print(' 1. Relevante tall utenom leie')
    print(' 2. Relative tall')
    print(' 3. Eiendomstall')
    print(' 4. Leietall')

    svar = int(input('Skriv inn tallet til ønsket output: '))

    #Utregning
    utregninger = verdi_utregning(boligdata)


    ###############
    #Sammenligning#
    ###############

    svar_test = False

    while svar_test == False:

        #Relevante tall     -       Sorterer etter "eoc"
        if svar == 1:
            svar_test = True
            boligliste = sammenlign_relevante_tall_ul(utregninger)

            for bolig in range(boligliste):
                eoc = boligliste[bolig][0]
                omløpsrate = boligliste[bolig][1]
                proi = boligliste[bolig][2]
                endring_egenkapital = boligliste[bolig][3]
                endring_egenkapital_prosent = boligliste[bolig][4]
                endring_egenkapital_prosent_per_år = boligliste[bolig][5]

                print(f'Bolig {bolig}   |   EOC: {eoc} - Omløpsrate: {omløpsrate} - PROI: {proi}   |   Fortjeneste: {endring_egenkapital} - Fortjeneste prosent: {endring_egenkapital_prosent} - Fortjeneste prosent per år: {endring_egenkapital_prosent_per_år}')


        #Relative tall      -       Sorterer etter "eoc"
        elif svar == 2:
            svar_test = True
            boligliste = sammenlign_relative_tall(utregninger)

            for bolig in range(boligliste):
                eoc = boligliste[bolig][0]
                omløpsrate = boligliste[bolig][1]
                proi = boligliste[bolig][2]

                print(f'Bolig {bolig}   |   EOC: {eoc} - Omløpsrate: {omløpsrate} - PROI: {proi}')
            

        #Eiendom            -       Sorterer etter "vekst_eiendomsverdi_prosent"
        elif svar == 3:
            svar_test = True
            boligliste = sammenlign_eiendom(utregninger)

            for bolig in range(boligliste):
                eiendomsverdi = boligliste[bolig][0]
                vekst_eiendomsverdi = boligliste[bolig][1]
                vekst_eiendomsverdi_prosent = boligliste[bolig][2]
                vekst_eiendomsverdi_prosent_per_år = boligliste[bolig][3]
                månedlige_renter = boligliste[bolig][4]
                total_renter_eiendom = boligliste[bolig][5]

                print(f'Bolig {bolig}   |   Kjøpsverdi: {eiendomsverdi}   |   Fortjeneste: {vekst_eiendomsverdi} - Fortjeneste prosent: {vekst_eiendomsverdi_prosent} - Fortjeneste prosent per år: {vekst_eiendomsverdi_prosent_per_år}   |   Månedlige renter: {månedlige_renter} - Totale renter: {total_renter_eiendom}')


        #Leietall           -       Sorterer etter "tilbakebetalt_lån"
        elif svar == 4:
            svar_test = True
            boligliste = sammenlign_leie(utregninger)

            for bolig in range(boligliste):
                tilbakebetalt_lån = boligliste[bolig][0]
                ny_lånesum = boligliste[bolig][1]
                månedlige_eierkostnader = boligliste[bolig][2]
                total_renter_leie = boligliste[bolig][3]

                print(f'Bolig {bolig}   |   Tilabkebetalt lån: {tilbakebetalt_lån} - Ny lånesum: {ny_lånesum}   |   Månedlige eierkostnader: {månedlige_eierkostnader} - Totale renter: {total_renter_leie')


        else:
            print('Ikke et gyldig valg.')
