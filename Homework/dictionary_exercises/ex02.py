#Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.
dicionario1 = {}
def nome_idade(nome,idade):
    if idade >=18:
        dicionario1 = {'nome': nome, 'idade': idade}
        return dicionario1
    else: 
        return {}
        
nome = (input('Digite o nome'))
idade = int(input('Digite a idade'))
resultado = nome_idade(nome,idade)
print(resultado)