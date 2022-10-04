
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {
            'a': '1',
            'b': '6',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 4*5?',
        'respostas': {
            'a': '1',
            'b': '20',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 5*5?',
        'respostas': {
            'a': '1',
            'b': '25',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 5+5?',
        'respostas': {
            'a': '1',
            'b': '10',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'{rk}){rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou!!')
        respostas_certas += 1
    else:
        print('Infelizmente, você errou!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(
    f'Você acertou um total de {respostas_certas} de {qtd_perguntas} questões.')
print(f'Porcentagem de acerto: {porcentagem_acerto}%')
