#Funksjon for aa regne renter lopende
#Rekursivt regne ut rentetotal

###################
# Renter - Maanedlig
###################

#Rentetest
def renter_test (laanesum, rentesats):
    return laanesum * rentesats

#Sum renter per maaned
def renter_rek_maan (laanesum, maanedlig_inntekt_m, total_maaneder, r):
    renter = (laanesum * (r - 1)) / 12                       #Regner renter
    ny_laanesum = (laanesum + renter) - maanedlig_inntekt_m    #Regner ny laanesum
    total_maaneder -= 1                                      #Trekker fra 1 maaned fra total

    if total_maaneder == 1:                                  #Sluttbetingelse
        return renter
    else:                                                   #Kaller seg selv med ny laanesum som parameter
        return renter + renter_rek_maan(ny_laanesum, maanedlig_inntekt_m, total_maaneder, r)

#Sum tilbakebetaling laan per maaned
def tilbakebetalt_rek_maan (laanesum, maanedlig_inntekt_m, total_maaneder, r):
    renter = (laanesum * (r - 1)) / 12                       #Regner renter
    ny_laanesum = (laanesum + renter) - maanedlig_inntekt_m    #Regner ny laanesum
    tilbakebetalt_sum = laanesum - ny_laanesum
    total_maaneder -= 1                                      #Trekker fra 1 maaned fra total

    if total_maaneder == 1:                                  #Sluttbetingelse
        return tilbakebetalt_sum
    else:                                                   #Kaller seg selv med ny laanesum som parameter
        return tilbakebetalt_sum + tilbakebetalt_rek_maan(ny_laanesum, maanedlig_inntekt_m, total_maaneder, r)


###############
# Vekst - aarlig
###############

#
def vekst_rek_aar (verdi, aar, veksttall):
    vekst = verdi * veksttall
    ny_verdi = verdi + vekst
    aar -= 1

    if aar == 1:
        return vekst
    else:
        return vekst + vekst_rek_aar(ny_verdi, aar, veksttall)