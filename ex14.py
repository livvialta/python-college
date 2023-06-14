produtos = {
    'banana' : 2.50,
    'maçã': 3.00,
    'laranja': 2.75,
    'abacaxi': 4.50,
    'manga':3.50
}

#imprimir o preço de uma maçã
print('O preço de uma maã é: R$'+ str(produtos['maçã']))
#Adicionar um novo produto
produtos['melancia'] = 6.00

#Imprimir todos os produtos e seus preços
for produtos, price in produtos.items():
    print(produtos + ': R$' + str(price))