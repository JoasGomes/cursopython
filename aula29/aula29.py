import sys
import time


def gera():
    # r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    # return r


def gera2():
    variavel = 'valor1'
    yield variavel
    variavel = 'valor2'
    yield variavel
    variavel = 'valor3'
    yield variavel


g = gera()
g2 = gera2()

print(hasattr(g, '__next__'))
print(hasattr(g, '__iter__'))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(g)
print(g2)

for v in g2:
    print(v)


lista = list(range(1000))
print(sys.getsizeof(lista))


lista2 = [x for x in range(1000)]
print(type(lista2))
print(sys.getsizeof(lista2))

lista3 = (x for x in range(1000))
print(type(lista3))
print(sys.getsizeof(lista3))
