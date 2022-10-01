"""
funções - def em python
"""


def saudacao(msg='olá', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '4')
    # print(msg, nome)
    return f'{msg} {nome}'


variavel = saudacao()
print(variavel)

saudacao()
saudacao('oi', 'joel')
saudacao('olá', 'vitor')


def funcao(var):
    print(var)


variavel2 = funcao('valor que eu quero')

if variavel2:
    print(variavel2)
else:
    print('nenhum valor')


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2


divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('conta inválida')


def dumb():
    return [1, 2, 3, 4, 5, 6, 7]


var = dumb()
print(var, type(var))


def tupla():
    return ('luiz', 'otavio')


var = tupla()

print(var, type(var))


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz {n} é divisivel por 3 e 5'
    if n % 5 == 0:
        return f'buzz {n} é divisivel por 5'
    if n % 3 == 0:
        return f'fizz {n} é divisivel por 3'
    return n


print(fb(7))
print(fb(13))
print(fb(15))
print(fb(22))
print(fb(9))
print(fb(25))
