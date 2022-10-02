
variavel = 'valor'


def funcao():
    print(variavel)


def funcao2(arg=None):
    # global variavel
    # variavel = 'outro valor'
    # print(variavel)
    arg = arg.replace('v', 'c')
    return arg


funcao()
outra_variavel = funcao2(arg=variavel)
print(outra_variavel)

print(variavel)


def func():
    # print(variavel) ----> erro usar antes de declarar
    variavel = 1234
    print(variavel)
    outra_variavel2 = 'joas vitor'
    return outra_variavel2


def func2(arg):
    print(arg)


var = func()
func2(var)


def ola_mundo():
    return 'olá mundo!'


def mestre(funcao_ola_mundo):
    return funcao_ola_mundo()


executando = mestre(ola_mundo)
print(executando)

# ------------------------------------- #


def mestre2(funcao_executada, *args, **kwargs):
    return funcao_executada(*args, **kwargs)


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando2 = mestre2(fala_oi, 'luiz')
executando3 = mestre2(saudacao, 'joas', 'dale')
print(executando3)
print(executando2)
