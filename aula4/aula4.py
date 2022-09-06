nome = 'Joás'
idade = 20
altura = 1.80
e_maior = idade > 18
peso = 80

imc = peso / (altura ** 2)
print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc)

# formatação de string
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))

# exercício

nome1 = 'josé'
idade1 = 40
altura = 1.90
peso1 = 90.5
ano_atual = 2022
nascimento = ano_atual - idade1

print(f'{nome1} tem {idade1} anos e {altura} de altura e {peso1}kg ')
print(f'{nome1} tem imc de {imc:.2f} e nasceu no ano de {nascimento}')


# entrada de dados

nomeInput = input("Qual o seu nome? ")
idadeInput = input("Qual sua idade? ")
print(f'o usuário digitou {nomeInput} e o tipo da variável é {type(nome)}')
print(f'{nomeInput} tem {idadeInput}')
