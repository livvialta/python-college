lista = []

for i  in range(10):
    num = int(input("Digite um número: "))

    lista.append(num)
    i += 1
        
maior = lista[0]
menor = lista[0]

for numMaior in lista:
    if numMaior > maior:
        maior = numMaior

for numMenor in lista:
    if numMenor < menor:
        menor = numMenor        

print("Os números digitados foram:", lista)
print("O maior e menor número digitados foram respectivamente:", maior,"e", menor)