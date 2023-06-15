#Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.
chave = ''
dicionario = {}
def maiorvalor(dicionario_funcao):
    maior_valor = max(dicionario_funcao.values())
    for chave,valor in dicionario_funcao.items():
        if valor == maiorvalor:
            return chave

while True:
    chave = str(input('Digite uma chave para representar um número:\n(se desejar parar digite "FIM")\n'))
    if chave == 'FIM':
        break
    valor = int(input('digite um número'))
    if chave not in dicionario and valor not in dicionario:
        dicionario[chave] = valor
    else:
        dicionario[chave] = valor
maiorvalor(dicionario_funcao)
    