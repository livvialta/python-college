#6- Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem decrescente.

n_elementos = int(input("Número de elementos na lista: \n"))

list = []

for i in range(n_elementos):

    numbers = int(input("Entre com um número."))
    list.append(numbers)

ordemDescre = sorted(list, reverse=True)
print(ordemDescre)



