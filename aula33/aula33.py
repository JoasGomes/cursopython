from itertools import count
from types import GeneratorType

"""exercício"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

"""solução mais python"""
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
print(list(zip(lista_a, lista_b)))

"""solução 1"""
# lista_soma = []
# for i in range(len(lista_b)):
#    lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

"""solução 2"""
# lista_soma = []
# for i, _ in enumerate(lista_b):
#    lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


variavel = zip('alo', 'alo')
# iterador que te entrega um de cada vez
print(next(variavel))
print(next(variavel))
print(next(variavel))

# checando se é gerador
print(isinstance(variavel, GeneratorType))

# é um gerador
variavel2 = ((x, y) for x, y in zip('alo', 'alo'))
print(variavel2)

print(isinstance(variavel2, GeneratorType))

"""
count - itertools
"""

# iterador sem fim, que começa em 5 e pula de 2 em 2
contador = count(start=5, step=2)

for valor in contador:
    print(valor)

    if valor > 10:
        break


contador1 = count()
lista = ['luiz', 'joas', 'bruna', 'maria', 'jose']
lista = zip(contador1, lista)
print(list(lista))

# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
