"""
manipulação de strings
* string indices
* fatiamento de strings
* funções built-in len, abs, type, print, etc.
"""
#       [012345]
texto = 'python'
print(texto[2])
#     [0123456789...]
url = 'www.google.com.br/'
print(url[:-1])

nova_string = url[2:6]
print(nova_string)
print(url[:6])

print(url[1:13:2])  # o último é a quantidade do salto

"""
estruturas de repetição
* while
"""

i = 0
while i < 10:
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1

print('acabou')

x = 0  # coluna

while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1

    x += 1

print('terminado!')

# mini calculadora

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair ? [s]im ou [n]ão')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar números')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')
