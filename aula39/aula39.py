"""
Módulos padrão do python
Funcionalidades padrão da linguagem
"""

import random
import sys

from app import PI, dobre_lista, lista, multiplica
from falaoi import fala_oi

for i in range(10):
    print(random.randint(0, 10))
print(sys.platform)


print(lista)
print(PI)


lista_main = [1, 2, 3, 4, 6, 7]
print(multiplica(lista_main))
print(dobre_lista(lista_main))


fala_oi()
