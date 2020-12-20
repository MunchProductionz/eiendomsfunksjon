#Funksjon for å regne renter løpende
#Rekursivt regne ut rentetotal

###################
# Renter - Månedlig
###################

#Rentetest
def renter_test (lånesum, rentesats):
    return lånesum * rentesats

#Sum renter per måned
def renter_rek_mån (lånesum, månedlig_inntekt_m, total_måneder, r):
    renter = (lånesum * (r - 1)) / 12                       #Regner renter
    ny_lånesum = (lånesum + renter) - månedlig_inntekt_m    #Regner ny lånesum
    total_måneder -= 1                                      #Trekker fra 1 måned fra total

    if total_måneder == 1:                                  #Sluttbetingelse
        return renter
    else:                                                   #Kaller seg selv med ny lånesum som parameter
        return renter + renter_rek_mån(ny_lånesum, månedlig_inntekt_m, total_måneder, r)

#Sum tilbakebetaling lån per måned
def tilbakebetalt_rek_mån (lånesum, månedlig_inntekt_m, total_måneder, r):
    renter = (lånesum * (r - 1)) / 12                       #Regner renter
    ny_lånesum = (lånesum + renter) - månedlig_inntekt_m    #Regner ny lånesum
    tilbakebetalt_sum = lånesum - ny_lånesum
    total_måneder -= 1                                      #Trekker fra 1 måned fra total

    if total_måneder == 1:                                  #Sluttbetingelse
        return tilbakebetalt_sum
    else:                                                   #Kaller seg selv med ny lånesum som parameter
        return tilbakebetalt_sum + tilbakebetalt_rek_mån(ny_lånesum, månedlig_inntekt_m, total_måneder, r)


###############
# Vekst - Årlig
###############

#
def vekst_rek_år (verdi, år, veksttall):
    vekst = verdi * veksttall
    ny_verdi = verdi + vekst
    år -= 1

    if år == 1:
        return vekst
    else:
        return vekst + vekst_rek_år(ny_verdi, år, veksttall)