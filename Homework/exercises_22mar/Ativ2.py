lista = []

for i  in range(10):
    palavra = int(input("Escreva algo! "))
    if palavra[0] == "a" or palavra[0] == "A":
        lista.append(palavra)
        i += 1
        


print("Os números digitados foram:", lista)