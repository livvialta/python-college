#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista com as chaves ordenadas em ordem alfabética.
dicionario1 = {'Bruno':43,'Junior': 87,'Maria':18, 'Ana':65}
def lista_alfabetica(dicionario):
    lista = []
    for chave,valor in dicionario.items():
        lista.append(chave)
    return sorted(lista)
print(lista_alfabetica(dicionario1))