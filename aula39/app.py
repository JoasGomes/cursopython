import math

PI = math.pi


def dobre_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


lista = [1, 2, 3, 4, 5]
print(dobre_lista(lista))
print(multiplica(lista))
print(PI)
