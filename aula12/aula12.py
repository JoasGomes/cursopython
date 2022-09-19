"""
listas em python
append, insert, pop, del, clear, extend, +
min, max
range
"""
booleanos = True
inteiros = 10
flutuante = -10.10
strings = 'textos'

texto = 'valor'
lista = [1, 2, 3, 4, 'joas vitor', True, 10]
print(lista)
lista[4] = 'joas'
print(lista)

print(lista[2:])
print('-----------------------------------')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
l4 = [1, 2, 3, 4, 5, 76, 7, 8, 9, 10]

l1.extend(l2)  # pega o valor de outra lista
l1.append('joas')  # adicionar um valor no final
l2.insert(0, 'banana')  # escolhe a posição e adiciona o valor
l2.pop()  # exclui último elemento
del (l2[3:5])  # exclui os valores das posições informadas

print(max(l4))  # mostra o maior valor da lista
print(min(l4))  # mostra o menor valor da lista

print(l1)
print(l2)
print(l3)

l5 = list(range(0, 100, 8))
print(l5)

for valor in l5:
    print(valor)

secreto = 'perfume'
digitadas = []
while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('digite apenas letras')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'existe {letra} na sua palavra secreta')
    else:
        print(f'a letra {letra} não existe na sua palavra')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    print(secreto_temporario)
