#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais alto na lista.
lista_numeros = input("Digite os números : ")

lista_numeros = [int(num) for num in lista_numeros.split(",")]

segundo_maior = sorted(set(lista_numeros))[-2]

print("O 2º maior número:", segundo_maior)