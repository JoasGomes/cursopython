# Operadores aritméticos
# +, -, *, /, //, **, %, ()

print('Multiplicação * ', 10 * 10)
print('Potenciação ** ', 10 ** 10)
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 10)
print('Divisão / ', 10 / 10)
print('Divisão arredondada // ', 10 // 10)
print('Resto da divisão ', 10 % 10)


# Variáveis

nome = 'Joás'
idade = 20  # int
altura = 1.80  # float
e_maior = idade > 18  # bool
peso = 80

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(idade * altura)

imc = peso / (altura ** 2)
print(nome, 'tem', idade, 'de idade e seu imc é:', imc)
