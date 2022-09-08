numInt = input('Digite um número inteiro: ')

try:
    numInt = int(numInt)
    if numInt % 2 == 0:
        print(f'{numInt} é par')
    else:
        print(f'{numInt} é impar')
except Exception:
    print('não é um numero inteiro')
# ----------------------------------------#

numero_inteiro = input('digite um numero inteiro')

if not numero_inteiro.isdigit():
    print('isso não é um número inteiro')
else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é impar')
    else:
        print(f'{numero_inteiro} é par')

# -----------------------------------------#

horaAtual = input('Digite a hora: ')
if horaAtual.isdigit():
    horaAtual = int(horaAtual)

    if horaAtual < 0 or horaAtual > 23:
        print('digite um horario valido')
    else:
        if horaAtual <= 11:
            print('bom dia')
        elif horaAtual <= 17:
            print('boa tarde')
        else:
            print('boa noite')
else:
    print('digite um horario entre 0 e 23')

# -----------------------------------------#

nomeUsuraio = input('Digite seu primeiro nome: ')

if nomeUsuraio.__len__() <= 4:
    print('seu nome é curto')
elif 6 >= nomeUsuraio.__len__() >= 5:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')
