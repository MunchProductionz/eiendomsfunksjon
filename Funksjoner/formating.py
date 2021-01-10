#0 desimaler
def f0 (tall):
    tall = float(tall)
    return format(tall, '.0f')


#1 desimal
def f1 (tall):
    tall = float(tall)
    return format(tall, '.1f')


#2 desimaler
def f2 (tall):
    tall = float(tall)
    return format(tall, '.2f')



#Pene Tall
def p(num):
    num_string = str(num)
    num_list = list(num_string)
    i = len(num_list) - 3

    while i > 0:
        num_list.insert(i , ' ')
        i -= 3

    return ''.join(num_list)
