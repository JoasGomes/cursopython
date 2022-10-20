from time import sleep, time


# explicação decoradores
def fala_oi():
    print('oi')


variavel = fala_oi
variavel()
print(type(variavel))


def master(funcao):
    def slave():
        print('agora estou decorada')
        funcao()
    return slave


var = master(fala_oi)
var()

# decoradores em python


def mater2(funcao):
    def slave2(*args, **kwargs):
        print('estou decorada')
        funcao(*args, **kwargs)
    return slave2


@mater2
def fala_oi2():
    print('oi')


@mater2
def outra_funcao(msg):
    print(msg)


outra_funcao('olá')
fala_oi2()

# -----------------------------#


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'a função {funcao.__name__} levou {tempo:.2f}ms para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)


demora()
