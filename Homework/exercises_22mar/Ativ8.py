#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.

n_elementos = int(input("Entre com o número de elementos que deseja adicionar a lista: \n"))

numeros = []
for i in range(n_elementos):
    num = int(input("Entre com um número: \n"))
    numeros.append(num)

for num in numeros:
    if num >= 10:
        print("Número:", num)
        num += 1
