from aula35 import lista, pessoas, produtos

print(produtos)
print(pessoas)
print(lista)

# mapea a lista e itera sobre ela retornando ja modificada
nova_lista = map(lambda x: x*2, lista)

# outra forma de fazer
# nova_lista = [x *2 for x in lista]
print(list(nova_lista))


for produto in produtos:
    print(produto)

# pegando os preços do dicionario produtos
precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)


# função pr aumentar 5% dos valores dos produtos
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


# tirando a idade de pessoas com o map
nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
