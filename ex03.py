dicionario = {'cat': 'chat', 'dog':'chien','horse':'cheval'}
for chave in dicionario.keys():#.keys simbolizam as chaves do dicionario então ele vai verificar todas as chaves ao inves dos valores
    print(chave, '->', dicionario[chave])