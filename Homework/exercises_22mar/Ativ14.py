#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais baixo na lista.

lista_numeros = input("Digite os numeros: ")

lista_numeros = [int(num) for num in lista_numeros.split(",")]

segundo_menor = sorted(set(lista_numeros))[1]

print("O 2º número mais baixo é:", segundo_menor)