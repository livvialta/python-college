#Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores, e retorna um dicionário criado a partir dessas listas.
lc = []
lv = []
def lista_dicionario(lista1, lista2):
    dicionario = {} 
    for count in range(n): #Como as lista tem o mesmo comprimento, o contador count estara na mesma posição nas duas listas
        dicionario[lista1[count]] = lista2[count] #Entao ele adiciona ao dicionario por exemplo valor[3] da lista 1 e valor[3] da lista 2  
    return dicionario
    
n = int(input('Digite o número de elementos que deseja nas listas: '))
for i in range(n):
    lc.append(input('Digite uma chave : '))
    lv.append(input('Digite um valor:'))                                                            
print(lista_dicionario(lc,lv))