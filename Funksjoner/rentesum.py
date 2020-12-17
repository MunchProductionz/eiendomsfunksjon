#Funksjon for å regne renter løpende
#Rekursivt regne ut rentetotal

#yeet

def renter_test (lånesum, rentesats):
    #Regne renter
    return lånesum * rentesats

def renter_rek (lånesum, inntekter, år, r):
    renter = lånesum * r
    ny_lånesum = (lånesum + renter) - inntekter
    år -= 1

    if år == 1:
        return renter
    else:
        return renter + renter_rek(ny_lånesum, inntekter, år, r)