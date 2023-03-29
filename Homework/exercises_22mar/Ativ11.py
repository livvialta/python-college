#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.
lista = []

for i in range(10):
    dado = int(input("Insira um valor: "))
    if dado % 2 == 1:
        lista.append(dado)
        i += 1

total = sum(lista)
print("Os números digitados foram:", lista)
print("O total dos números ímpares digitados foram:", total)