#Sammenligning data

#listeliste[i] = [

# [eoc,
# omlopsrate,
# proi],

# [endring_egenkapital,
# endring_egenkapital_prosent,
# endring_egenkapital_prosent_per_aar,

# [eiendomsverdi,
# vekst_eiendomsverdi,
# vekst_eiendomsverdi_prosent,
# vekst_eiendomsverdi_prosent_per_aar,
# maanedlige_renter,
# total_renter_eiendom],

# [tilbakebetalt_laan,
# ny_laanesum,
# maanedlige_eierkostnader,
# totale_renter_leie],
# 
# [lenke] 

# ]


#Sammenligner relevante tall - eoc
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



#Sammenligner relative tall - eoc
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



#Sammenligner eiendomstall - vekst_eiendomsverdi_prosent
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



#Sammenligner leietall - tilbakebetalt_laan
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



#Problemer med aa sortere liste = [[tilb...1, ...], [tilb...2, ...], ...]
#Maa sortere liste basert paa [tilb...1, tilb...2, ...]
#Sorterer etter l[0] (dvs. forste element)

#leietall = sorted(leietall, key=lambda l:l[0], reverse = False)