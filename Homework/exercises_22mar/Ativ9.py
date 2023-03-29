#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.

n_elementos = int(input("Entre com a quantidade de elementos que você quer na lista: \n"))

numeros = []

for i in range(n_elementos):
    num = int(input("Entre com um número: \n"))
    numeros.append(num)

for num in numeros:
    if num < 5:
        print("Valor menor que 5: %i" % (num))
        num += 1
    
