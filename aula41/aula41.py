
# w+ --> trabalha com leitura e escrita
file = open('abc.txt', 'w+')

# função para escrever no arquivo
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.write('Linha 4\n')

# função que volta o cursor pra o início do arquivo
file.seek(0, 0)

# função para ler no arquivo
print('lendo linhas')
print(file.read())
print('#############')

file.seek(0, 0)
# vai ler o arquivo por linha
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#############')

file.seek(0, 0)
# vai ler o arquivo e retornar uma lista com eles
for linha in file.readlines():
    print(linha, end='')
# print(file.readlines())

file.close()
