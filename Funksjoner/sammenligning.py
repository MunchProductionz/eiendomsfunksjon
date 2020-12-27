#Sammenligning data

#listeliste[i] = [

# [eoc,
# omløpsrate,
# proi],

# [endring_egenkapital,
# endring_egenkapital_prosent,
# endring_egenkapital_prosent_per_år],

# [eiendomsverdi,
# vekst_eiendomsverdi,
# vekst_eiendomsverdi_prosent,
# vekst_eiendomsverdi_prosent_per_år,
# månedlige_renter,
# total_renter_eiendom],

# [tilbakebetalt_lån,
# ny_lånesum,
# månedlige_eierkostnader,
# totale_renter_leie]

# ]


#Sammenligner relevante tall - eoc
def sammenlign_relevante_tall_ul (listeliste):

    ##########
    #Variabler
    ##########

    #eoc = listeliste[i][0][0]
    #omløpsrate = listeliste[i][0][1]
    #proi = listeliste[i][0][2]

    #endring_egenkapital = listeliste[i][1][0]
    #endring_egenkapital_prosent = listeliste[i][1][1]
    #endring_egenkapital_prosent_per_år = listeliste[i][1][2]
    relevante_tall_ul = []


    ###################
    #Sortere etter eoc#
    ###################

    for liste in listeliste:
            eoc = liste[0][0]
            omløpsrate = liste[0][1]
            proi = liste[0][2]
            endring_egenkapital = liste[1][0]
            endring_egenkapital_prosent = liste[1][1]
            endring_egenkapital_prosent_per_år = liste[1][2]

            relevante_tall_ul.append(eoc)
            relevante_tall_ul.append(omløpsrate)
            relevante_tall_ul.append(proi)
            relevante_tall_ul.append(endring_egenkapital)
            relevante_tall_ul.append(endring_egenkapital_prosent)
            relevante_tall_ul.append(endring_egenkapital_prosent_per_år)

    relevante_tall_ul.sort(key=takeFirst)       #Problemer med å sortere tot = [[eoc1, ...], [eoc2, ...], ...]
                                                #Må sortere tot basert på [eoc1, eoc2, ...]
    return relevante_tall_ul



#Sammenligner relative tall - eoc
def sammenlign_relative_tall (listeliste):

    ##########
    #Variabler
    ##########

    #eoc = listeliste[i][1][0]
    #omløpsrate = listeliste[i][1][1]
    #proi = listeliste[i][1][2]
    relative_tall = []


    ###################
    #Sortere etter poc#
    ###################

    for liste in listeliste:
        eoc = liste[0][0]
        omløpsrate = liste[0][1]
        proi = liste[0][2]

        relative_tall.append(eoc)
        relative_tall.append(omløpsrate)
        relative_tall.append(proi)

    relative_tall.sort(key=takeFirst)       #Problemer med å sortere tot = [[eoc1, ...], [eoc2, ...], ...]
                                            #Må sortere tot basert på [eoc1, eoc2, ...]
    return relative_tall



#Sammenligner eiendomstall - vekst_eiendomsverdi_prosent
def sammenlign_eiendom (listeliste):

    ##########
    #Variabler
    ##########

    #eiendomsverdi = listeliste[i][2][0]
    #vekst_eiendomsverdi = listeliste[i][2][1]
    #vekst_eiendomsverdi_prosent = listeliste[i][2][2]
    #vekst_eiendomsverdi_prosent_per_år = listeliste[i][2][3]
    #månedlige_renter = listeliste[i][2][4]
    #total_renter_eiendom = listeliste[i][2][5]
    eiendomstall = []


    #####################################
    #Sortere etter vekst_eiendomsverdi_prosent#
    #####################################

    for liste in listeliste:
        eiendomsverdi = liste[2][0]
        vekst_eiendomsverdi = liste[2][1]
        vekst_eiendomsverdi_prosent = liste[2][2]
        vekst_eiendomsverdi_prosent_per_år = liste[2][3]
        månedlige_renter = liste[2][4]
        total_renter_eiendom = liste[2][5]

        eiendomstall.append(eiendomsverdi)
        eiendomstall.append(vekst_eiendomsverdi)
        eiendomstall.append(vekst_eiendomsverdi_prosent)
        eiendomstall.append(vekst_eiendomsverdi_prosent_per_år)
        eiendomstall.append(månedlige_renter)
        eiendomstall.append(total_renter_eiendom)

    eiendomstall.sort(key=takeSecond)       #Problemer med å sortere tot = [[vekst...1, ...], [vekst...2, ...], ...]
                                            #Må sortere tot basert på [vekst...1, vekst...2, ...]

    return eiendomstall



#Sammenligner leietall - tilbakebetalt_lån
def sammenlign_leie (listeliste):

    ##########
    #Variabler
    ##########

    #tilbakebetalt_lån = listeliste[i][3][0]
    #ny_lånesum = listeliste[i][3][1]
    #månedlige_eierkostnader = listeliste[i][3][2]
    #total_renter_leie = listeliste[i][3][3]
    leietall = []


    #################################
    #Sortere etter tilbakebetalt_lån#
    #################################

    for liste in listeliste:
        tilbakebetalt_lån = liste[3][0]
        ny_lånesum = liste[3][1]
        månedlige_eierkostnader = liste[3][2]
        total_renter_leie = liste[3][3]

        leietall.append(tilbakebetalt_lån)
        leietall.append(ny_lånesum)
        leietall.append(månedlige_eierkostnader)
        leietall.append(total_renter_leie)

    leietall.sort(key=takeFirst)        #Problemer med å sortere tot = [[tilb...1, ...], [tilb...2, ...], ...]
                                        #Må sortere tot basert på [tilb...1, tilb...2, ...]

    return leietall