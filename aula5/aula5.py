# condicionais

if False:  # valor verdadeiro já dado
    print("Verdadeiro")

    num_1 = 2
    num_2 = 4
    print(num_1 + num_2)
elif True:
    print("agora é verdadeiro")
    nome = input("Qual seu nome? ")
    print(f"seu nome é {nome}")
else:
    print("Não é verdadeira")


# operadores relacionais

# == igualdade
# > maior que
# >= maior ou igual
# < menor que
# <= menor ou igual
# != diferente

num1 = 2  # int
num2 = 2  # int

expressao = (num1 == num2)

print(expressao)  # true

nomeUsuario = input("Seu nome: ")
idade = int(input("Qual sua idade? "))

idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nomeUsuario} pode pegar o empréstimo")
else:
    print(f"{nomeUsuario} não pode pegar o emprestimo")


# operadores lógicos

carro = 'lambo'
moto = 'bmw'

if carro == 'lambo' and moto == 'bmw':
    print('as duas sao verdadeiras')
else:
    print('tem algo errado')


if carro == 'lambo' or moto == 'ducati':
    print("pelo menos uma é vdd")
else:
    print("as duas estão erradas")


nomeTeste = 'joas vitor'

if "u" in nomeTeste:
    print('existe u no seu nome')
else:
    print('nao existe u no seu nome')
