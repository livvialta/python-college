#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, verifique se um determinado nome está na lista. Se estiver, imprima "O nome está na lista"; caso contrário, imprima "O nome não está na lista".
nomes = input("Digite os nomes: ").split(",")

nome_procurado = input("Digite o nome a ser procurado: ")

if nome_procurado in nomes:
    print("O nome está na lista")
else:
    print("O nome não está na lista")