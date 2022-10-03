
d1 = {'chave1': 'valor da chave'}
d1['nova-chave'] = 'valor da nova chave'
d2 = dict(chave1='valor um da chave do d2', chave2='valor dois')

print(d1)
print(d1['nova-chave'])
print(d2['chave2'])

dic = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'tupla',
}
print('str' in dic)
print('str' in dic.keys())
print('valor' in dic.values())

dic['naoexiste'] = 'agora existe'

if 'naoexiste' in dic:
    print(dic['naoexiste'])

print(dic.get('nomedachave'))  # não existe ==> none
print(dic[(1, 2, 3, 4)])


clientes = {
    'cliente1': {
        'nome': 'joão',
        'sobrenome': 'paulo'
    },
    'cliente2': {
        'nome': 'joás',
        'sobrenome': 'vitor'
    },
    'cliente3': {
        'nome': 'pedro',
        'sobrenome': 'vitor'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


um_dicionario = {
    1: 2,
    2: 3,
    3: 4,
}

novo_dicionario = {
    'a': 'b',
    'c': 'd',
}

um_dicionario.update(novo_dicionario)
print(um_dicionario)
