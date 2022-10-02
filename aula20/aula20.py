# lambda
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


# lista.sort(key=func, reverse=True)
lista.sort(key=lambda item: item[1])
print(lista)

# tupla
t1 = (1, 2, 3, 'a', 'luiz')
print(t1)

for v in t1:
    print(v)


t2 = 6, 7, 8, 9, 10
t3 = t1 + t2

n1, n2, n3, *_, n10 = t3

print(n3)
print(_)

t_tupla = 1, 2, 3, 4, 5
t_tupla = list(t_tupla)
t_tupla[1] = 123434
print(t_tupla)
