lista = []
num = int(input("Escreva um número: "))

for i  in range(10):
    dado = int(input("Insira um valor: "))
    if dado % num == 0:
        lista.append(dado)
        i += 1
        


print("Os números digitados foram:", lista)