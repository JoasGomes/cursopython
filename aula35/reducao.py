from functools import reduce

from aula35 import lista, pessoas, produtos

# acumulador básico
# acumula = 0
# for item in lista:
#    acumula += item
# print(acumula)

# recebe um acumulador que começa com 0
# todos os itens que forem sendo iterados vão somando com o acumulador
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)  # soma dos elementos da lista acumulados

# reduzindo o dicionario produtos somando os preços dele
soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

# somando as idades de pessoas
soma_idades = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idades)
