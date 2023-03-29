# Pedir ao usuário para digitar uma lista de palavras
palavras = input("Digite uma lista de palavras, separadas por vírgula: ")

# Converter a string em uma lista de palavras
palavras = palavras.split(",")

# Criar uma nova lista de palavras que têm um número ímpar de letras
impares = [palavra for palavra in palavras if len(palavra) % 2 != 0]

# Imprimir a nova lista
print("Lista de palavras com número ímpar de letras:", impares)