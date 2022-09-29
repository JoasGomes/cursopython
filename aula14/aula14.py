"""
for / else em python
"""

variavel = ['luiz', 'joas', 'maria']

comeca_com_j = False

for valor in variavel:
    print(valor)
    if valor.startswith('j'):
        print('começa com j', valor)
    else:
        print('não começa com j', valor)
    if valor.startswith('j'):
        comeca_com_j = True
    print(comeca_com_j)

if comeca_com_j:
    print('existe uma palavra com j')
else:
    print('não existe uma palavra com j')


for valor2 in variavel:
    print(valor2)
    if valor2.startswith('j'):
        break
else:
    print("não existe uma que comece com j")
