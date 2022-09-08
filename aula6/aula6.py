usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('voce precisa de pelo menos 6 caracteres')
else:
    print('voce foi cadastrado no sistema')


string1 = input('digite algo: ')
string2 = input('digite outra coisa: ')

print(
    f'a quantidade total de caracteres digitados foi de {len(string1) + len(string2)}')

print(len(string2))
print(string2.__len__())


# funções nativas

num1 = input('digite um número: ')
num2 = input('digite outro número: ')
# isnumeric isdigit isdecimal

# números e positivos
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('nao pude realizar contas')


# placeholder
valor = True

if valor:
    pass
else:
    print('tchau')
