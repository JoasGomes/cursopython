
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='joas', a6='5')
print(var[0], var[1])


def args(*args):
    args = list(args)
    args[0] = 20
    print(args)
    print(args[0])
    print(args[1])
    print(len(args))


args(1, 2, 3, 4, 5, 6, 7, 8)

lista = [1, 2, 3, 4, 5]
lista3 = [10, 20, 30, 40, 50]
n1, n2, *n = lista
print(n1, n2, n)

lista2 = [1, 2, 3, 4]
print(*lista2, sep='-')


def funcao(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('não temos idade')


funcao(*lista, *lista3, nome='luiz', sobrenome='vitor')
