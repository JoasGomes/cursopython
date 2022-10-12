"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

from itertools import count, zip_longest

# código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

# código
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)
# print(next(cidades_estados))
for v in cidades_estados:
    print(v)

"""zip_longest"""

# código2
cidades2 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'outra']

# código2
estados2 = ['SP', 'MG', 'BA']

cidades_estados2 = zip_longest(cidades2, estados2, fillvalue='estado')
# print(next(cidades_estados))
for v in cidades_estados2:
    print(v)

indice = count()
cidades3 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'outra']
estados3 = ['SP', 'MG', 'BA']

cidades_estados3 = zip(indice, cidades3, estados3)
# print(next(cidades_estados))
# print(list(cidades_estados3))

for indice, cidade, estado in cidades_estados3:
    print(indice, estado, cidade)
