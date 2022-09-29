"""
split, join, enumerate em python
* split - dividir uma string #str
* join - juntar uma lista #str
* enumerate - enumerar elementos da lista #list / iteráveis
"""

string = "o brasil é o país do futebol, o brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    # print(valor)
    # print(f'a palavra {valor} apareceu {lista_1.count(valor)}x na frase')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'a palavra que apareceu mais vezes é {palavra} ({contagem}x)')


string2 = 'o brasil é penta'
lista_3 = string2.split(' ')
string3 = ','.join(lista_3)

print(string3)


stringEnum = 'o brasil é penta'
lista_enum = stringEnum.split(' ')

for indice, valor in enumerate(lista_enum):
    print(indice, valor, lista_enum[indice])


lista_numeros = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in lista_numeros:
    print(v[0], v[1])
