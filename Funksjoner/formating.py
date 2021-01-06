#0 desimaler
def f0 (tall):
    return format(tall, '.0f')


#1 desimal
def f1 (tall):
    return format(tall, '.1f')


#2 desimaler
def f2 (tall):
    return format(tall, '.2f')



#Pene Tall
def p (tall):
    streng = str(tall)

    for mellomrom in range(len(streng), 0, -3):
        penere_tall = streng[:mellomrom] + ' ' + streng[mellomrom:]     #Problem
                                                                        #Fjerner mellomrom som er lagt til i slutten av strengen
    return penere_tall
