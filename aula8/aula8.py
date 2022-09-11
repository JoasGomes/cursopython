"""
formatando valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(numeros)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro

"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num_3 = 1
num_4 = 1234
print(f'{num_3:0>10}')  # 10 casas decimais ao todo
print(f'{num_4:0<10}')  # direita
print(f'{num_4:0^10}')  # centro

nome = 'joás vitor paiva'
sonbrenome = 'gomes'
qualquer_assunto = 'é bonito'
nome_sobre_assunto = '{0} {1}, {2}'.format(nome, sonbrenome, qualquer_assunto)
print(nome_sobre_assunto)

print((50-len(nome)) / 2)
print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

print(nome.lower())
print(nome.upper())
print(nome.title())
