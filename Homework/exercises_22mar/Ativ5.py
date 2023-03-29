lista = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)


listaOrdenada = sorted(lista)

print("Lista digitada pelo usuário:", lista,"\nLista ordenada:", listaOrdenada)