"""
exemplo:
    [1,2,3,3,2,1] -> 1,2,3 são duplicados(retorne 3)
    [1,2,3,4,5,6] -> retorne -1 (não tem duplicados)
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 2, 3, 4, 1, 4, 5, 6, 7, 8],
    [1, 3, 4, 4, 5, 6, 7, 3, 2, 4],
    [6, 4, 5, 6, 8, 9, 0, 1, 12, 2],
    [2, 3, 4, 2, 4, 6, 7, 4, 6, 7],
    [1, 5, 6, 3, 2, 1, 4, 6, 7, 8],
    [9, 7, 5, 8, 2, 3, 9, 5, 6, 8],
    [1, 2, 3, 4, 4, 3, 2, 4, 6, 8],
]


def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))
