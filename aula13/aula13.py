secreto_temporario = ''

"""
    secreto_temporario += 'a'
    secreto_temporario += 'b'
    secreto_temporario += '*'

    print(secreto_temporario)
"""

secreto = 'python'

digitadas = ['p', 'y', 't', 'h', 'o', 'n']

# for letra_secreta in secreto:
#    print(letra_secreta)

for letra_secreta in secreto:
    print(f'iteração para a letra {letra_secreta}')

    if letra_secreta in digitadas:
        print(f'a letra que eu queria {letra_secreta}')
        secreto_temporario += letra_secreta
    else:
        print(f'essa letra eu nao queria {letra_secreta}')
        secreto_temporario += '*'
    print('secreto_temporario=', secreto_temporario)
print(secreto_temporario)

if secreto == secreto_temporario:
    print('você ganhou!!')
