from vendas.calc_precos import aumento, reducao
from vendas.formata.preco import real

preco = 49.90
preco_aumentado = aumento(preco, 15, formata=True)
print(preco_aumentado)


preco_reduzido = reducao(preco, 15, formata=True)
print(preco_reduzido)

print(real(50))
