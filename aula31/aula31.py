
carrinho = []

carrinho.append(('produto 1', 30.50))
carrinho.append(('produto 2', '20'))
carrinho.append(('produto 3', 60))

print(carrinho)

# total = []
# for produto in carrinho:
#    total.append(produto[1])
# print(sum(total))

total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)
