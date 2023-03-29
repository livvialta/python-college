#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.

nomes = []

while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): \n")
    if nome == 'fim':
        break
    nomes.append(nome)

# Encontra o nome mais longo e o nome mais curto da lista
nome_mais_longo = max(nomes, key=len)
nome_mais_curto = min(nomes, key=len)

print("O nome mais longo é:", nome_mais_longo)
print("O nome mais curto é:", nome_mais_curto)