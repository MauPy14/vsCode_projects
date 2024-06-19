import random
def gen_pass(lenght):
    x = lenght
    elements = 'qwertyuiopasdfghjklñzxcvbnm-+/*!&$=?#<>QWERTYUIOPASDFGHJKLÑZXCVBNM'
    clave = ''
    for i in range(x):
        clave += random.choice(elements)

    return clave