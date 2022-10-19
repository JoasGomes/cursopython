"""
w+ => ler e escrever mas apaga tudo e cria do 0
a+ => adiciona algo mas não apaga oq estava lá
"""
import json

try:
    file = open('abcde.txt', 'w+')
    file.write('linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

# com esse modo não preciso fechar o arquivo
with open('xyz.txt', 'w+') as file:
    file.write('linha1\n')
    file.write('linha2\n')
    file.write('linha3\n')

    file.seek(0)
    print(file.read())


d1 = {
    'Pessoa 1': {
        'nome': 'joas',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'vitor',
        'idade': 45,
    },
}

print(d1)
d1_json = json.dumps(d1)
print(d1_json)

with open('jjj.json', 'w+') as file:
    file.write(d1_json)
