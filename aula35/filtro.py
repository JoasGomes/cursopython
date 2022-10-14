from aula35 import lista, pessoas, produtos

# vai iterar sobre a lista e checar a condição e retorna oq for true
nova_lista = filter(lambda x: x > 5, lista)

# forma de fazer com list comprehension
# nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))

# iterando e vendo quais preços são maiores que 50
novo_produto = filter(lambda p: p['preco'] > 50, produtos)

for produto in novo_produto:
    print(produto)

print()

# filtrando pessoas com o nome = joas e fazando o loop pelos resultados
nova_pessoa = filter(lambda p: p['nome'] == 'joas', pessoas)
for pessoa in nova_pessoa:
    print(pessoa)

print()

# filtrando maiores de idade
maiores_idade = filter(lambda p: p['idade'] >= 18, pessoas)
for adultos in maiores_idade:
    print(adultos)
