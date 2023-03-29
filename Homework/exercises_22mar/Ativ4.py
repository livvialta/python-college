lista = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

total = sum(lista)

media = total / len(lista)

print("Os valores digitados foram:", lista)
print("A soma dos dados é:", total)
print("A média dos valores da lista é:", media)