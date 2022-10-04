# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5}
s2 = set()
s2.add(1)  # adiciona
s2.add(2)
s2.add((1234, 'joas'))

s2.discard(2)  # descarta(remove)
s2.update('Python')  # adiciona iterando('p', 'y', 't', 'h', 'o', 'n')
s2.update([1, 2, 3, 4, 5], {5, 4, 6, 7, 8})  # geralmente ultiliza-se assim

print(s2)

for v in s1:
    print(v)

l1 = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 4, 4, 'joas', 'joas']
l1 = set(l1)  # transformando em um set

print(l1)  # elementos duplicados serão removidos

set1 = {1, 2, 3, 4, 10}
set2 = {1, 2, 3, 4, 5, 6}
set3 = set1 | set2  # vai unir os sets sem duplica-los
set4 = set1 & set2  # mostra elementos presentes em ambos
set5 = set1 - set2  # mostra elementos que só estão no da esquerda
set6 = set1 ^ set2  # exclusivos de cada set

print(set3)
print(set4)
