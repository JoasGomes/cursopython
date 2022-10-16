
try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro.')
    print(a[1])
except NameError as erro:
    print('erro do desenvolvedor', erro)
except (IndexError, KeyError) as erro:
    print('erro do indice ou de chave.', erro)
except Exception as erro:
    print('ocorreu um erro inesperado.', erro)
else:
    print('seu código foi executado com sucesso.')
    print(a)
finally:
    print('vai ser executado sempre.')

print('continua...')
