
l1 = [1, 2, 3, 4, 5]
l2 = [v*2 for v in l1]
print(l2)


lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
    ('chave4', 'valor4'),
]

d1 = {x: y for x, y in lista}
d2 = dict(lista)

m1 = {x*2: y*2 for x, y in lista}
print(m1)

print(d1)
print(d2)


ex1 = {x: y for x, y in enumerate(range(5))}
print(ex1)

ex2 = {f'chave{x}': x**2 for x in range(5)}
print(ex2, type(d1))
