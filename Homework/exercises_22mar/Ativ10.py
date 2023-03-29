#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.

n_elementos = int(input("Entre com a quantidade de elementos que você quer na lista: \n"))

lista = []
lista_sem_duplicatas = []

for i in range(n_elementos):
    num = int(input("Entre com um número: \n"))
    lista.append(num)

#Usando um loop while para percorrer a lista e remover os elementos duplicados
while lista:
    elemento = lista.pop(0) #pop() é usado para remover elemento. 
    
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)

#Imprimindo resultado
print('A lista está sem elementos duplicados:', lista_sem_duplicatas)
    
    