#Sammenligning data

#listeliste[i] = [endring_egenkapital, eiendomsverdi, vekst_eiendomsverdi, månedlige renter, total_renter, ny_lånesum, månedlige_eierkostnader, totale_renter_leie]


#Sammenligner eiendomstall
def sammenlign_eiendom (listeliste):

    ##########
    #Variabler
    ##########

    #endring_egenkapital = listeliste[i][0]
    #eiendomsverdi = listeliste[i][1]
    #vekst_eiendomsverdi = listeliste[i][2]
    #månedlige_renter = listeliste[i][3]
    #total_renter = listeliste[i][4]
    rad = []


    ##################################
    #Sortere etter endring_egenkapital
    ##################################

    for liste in listeliste:
        endring_egenkapital = liste[0]
        eiendomsverdi = liste[1]
        vekst_eiendomsverdi = liste[2]
        månedlige_renter = liste[3]
        total_renter = liste[4]

        rad.append(endring_egenkapital)
        rad.append(eiendomsverdi)
        rad.append(vekst_eiendomsverdi)
        rad.append(månedlige_renter)
        rad.append(total_renter)

    rad.sort(key=takeFirst)

    return rad


#Sammenligner leietall
def sammenlign_leie (listeliste):

    ##########
    #Variabler
    ##########

    #ny_lånesum = listeliste[i][5]
    #månedlige_eierkostnader = listeliste[i][6]
    #total_renter_leie = listeliste[i][7]
    rad = []


    ################################
    #Sortere etter tilbakebetalt_lån
    ################################

    for liste in listeliste:
        ny_lånesum = liste[5]
        månedlige_eierkostnader = liste[6]
        total_renter_leie = liste[7]

        rad.append(ny_lånesum)
        rad.append(månedlige_eierkostnader)
        rad.append(total_renter_leie)

    rad.sort(key=takeFirst)

    return rad