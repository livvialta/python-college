#Escreva uma função que receba um dicionário como entrada e retorna duas listas. Uma com chave e outra com valor.
dicionario1 = {'Bruno':12, 'José':23, 'Junior':56}
def dicionario_lista(dicionario):
    lista = []
    lista1 = []
    for chave, valor in dicionario.items():#Ele verifica as chaves e os valores nos items do dicionario
        lista.append(chave)#E aqui adiciona em uma lista apenas as chaves
        lista1.append(valor)#Aqui apenas os valores
    return lista,lista1

print(dicionario_lista(dicionario1))