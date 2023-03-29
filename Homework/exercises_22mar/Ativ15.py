#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, remova todos os números duplicados da lista e imprima a nova lista.

lista_numeros = input("Digite os numeros: ")

lista_numeros = [int(num) for num in lista_numeros.split(",")]

nova_lista = list(set(lista_numeros))

print("A nova lista é:", nova_lista)