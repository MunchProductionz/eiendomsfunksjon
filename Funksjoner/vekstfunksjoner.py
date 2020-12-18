#Funksjon for å regne renter løpende
#Rekursivt regne ut rentetotal

###################
# Renter - Månedlig
###################

def renter_test (lånesum, rentesats):
    return lånesum * rentesats

def renter_rek_mån (lånesum, månedlig_inntekt_m, total_måneder, r):
    renter = (lånesum * (r - 1)) / 12                   #Regner renter
    ny_lånesum = (lånesum + renter) - inntekter         #Regner ny lånesum
    total_måneder -= 1                                  #Trekker fra 1 måned fra total

    if total_måneder == 1:                              #Sluttbetingelse
        return renter
    else:                                               #Kaller seg selv med ny lånesum som parameter
        return renter + renter_rek(ny_lånesum, månedlig_inntekt_m, total_måneder, r)


###############
# Vekst - Årlig
###############

def vekst_rek_år (lånesum, år, veksttall):
    vekst = lånesum * veksttall
    ny_lånesum = lånesum + vekst
    år -= 1

    if år == 1:
        return renter
    else:
        return renter + renter_rek(ny_lånesum, år, r)