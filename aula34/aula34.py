"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, groupby, permutations, product, tee

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'João', 'Maurício']

# ordem não importa
for grupo in permutations(pessoas, 2):
    print(grupo)

# ordem importa
for grupo in combinations(pessoas, 2):
    print(grupo)

# pode nome com o mesmo nome
for grupo in product(pessoas, repeat=2):
    print(grupo)


alunos = [
    {'nome': 'luiz', 'nota': 'a'},
    {'nome': 'bruno', 'nota': 'b'},
    {'nome': 'junior', 'nota': 'd'},
    {'nome': 'joas', 'nota': 'c'},
    {'nome': 'vitor', 'nota': 'b'},
    {'nome': 'laura', 'nota': 'd'},
    {'nome': 'julia', 'nota': 'a'},
    {'nome': 'paula', 'nota': 'c'},
    {'nome': 'ana', 'nota': 'b'},
    {'nome': 'aline', 'nota': 'e'},
]
def ordena(item): return item['nota']


alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiram a nota {agrupamento}')

# for aluno in alunos:
#     print(aluno)
