"""
for in em python
iteração em strings com for
"""
texto = 'python'

for n, letra in enumerate(texto):
    print(n, letra)

# fução range(start=0, stop, step=1)
for r in range(20, 9, -1):
    print(r)

print('#############')

for m in range(100):
    if m % 8 == 0:
        print(m)

textinho = 'python'
nova_string = ''

for letra in textinho:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
