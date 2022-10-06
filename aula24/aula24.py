# iteração for sobre sequências
""" tupla1 = (2, 3, 4, 5)
for var in tupla1:
    print(var)

tupla2 = [10, 20, 30]
tupla2[0] = 900
for v in tupla2:
    print(v)

for vogal in "eiaou":
    print(vogal) """


""" entrada = input()
for letra in entrada:
    if ord(letra) > 90:
        print('o valor unicode da letra é maior que 90') """

""" tupla_2 = [10, 20, 30]
for v in tupla_2:
    print(tupla_2)


for x in range(8):
    print('oi') """

""" for i in range(2, 8):
    print('olá') """

""" for x in range(2, 8, 2):
    print('iae') """

""" for c in range(8, 2, -1):
    print('dale') """

""" entrada = input()
if (entrada[0].lower() in "aeiou"):
    print('o primeiro valor esta em "aeiou"')
else:
    print('o primeiro valor nao esta em "aeiou') """

""" entrada = input()
if entrada[-7:] == ".gov.br":
    print('deu certo')
else:
    print('deu errado') """


""" entrada = input().split()
if entrada[0] > entrada[1]:
    print('valor 1 maior quem o valor 2')
else:
    print('infelizmente nao deu certo') """


entrada = [int(x) for x in input().split()]
print(entrada)
entrada.extend([int(z) for z in input().split()])
print(entrada)
