# while com else

contador = 50
acumulador = 2

while contador < 100:
    print(contador)
    contador += acumulador


contador1 = 1
acumulador1 = 1

while contador1 <= 10:
    print(contador1, acumulador1)

    acumulador1 = acumulador1 + contador1
    contador1 += 1
else:
    print('cheguei no else')

print('cheguei no fim.')


# strings com while

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador2 = 0
print(frase[5])
print(tamanho_frase)

nova_string = ''

while contador2 < tamanho_frase:
    print(frase[contador2], contador2)
    nova_string += frase[contador2]
    contador2 += 1

print(nova_string)
