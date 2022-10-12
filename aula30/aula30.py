# listas, tuplas, strings -> sequencias -> iteráveis
nome = 'joas vitor'
iterador = iter(nome)
# gerador = (letra for letra in nome)

# print(next(gerador))  # j
# print(next(gerador))  # o
# print(next(gerador))  # a
# print(next(gerador))  # s
# print(next(gerador))

# print('o for começou')

# vai consumir do 'v' em diante
# for letra in gerador:
#    print(letra)

try:
    print(next(iterador))  # j
    print(next(iterador))  # o
    print(next(iterador))  # a
    print(next(iterador))  # s
    print(next(iterador))
    print(next(iterador))  # v
    # print(next(iterador))  # i
    # print(next(iterador))  # t
    # print(next(iterador))  # o
    # print(next(iterador))  # r
except Exception:
    pass

# consumi os valores até o 'v'
print('cade os valores ?')
for valor in iterador:
    print(valor)

# for letra in nome:
#    print(letra)
#
# print('#' * 10)
#
# for letra in nome:
#    print(letra)
#
# print(nome)
