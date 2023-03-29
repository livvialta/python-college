lista = []

for i  in range(10):
    nome = input("Digite um número: ")
    cont = nome.find("e")
    if cont > -1:
        lista.append(nome)
        i += 1
        


print("Os números digitados foram:", lista)