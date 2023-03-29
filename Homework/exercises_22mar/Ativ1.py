#Criando a lista com dados do usuário
lista = []

for i  in range(10):
    dado = int(input("Insira um valor: "))
    if dado % 2 == 0:
        lista.append(dado)
        i += 1
        


print("Os números digitados foram:", lista)