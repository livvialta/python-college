cadastro = {}
while True:
    nome = str(input('digite o nome completo:'))
    if nome == '':
        break
    idade = int(input('digite a idade'))
    cidade = input('Digite a cidade')
    
#Adiciona os dados ao dicionario
    cadastro[nome] = {'idade': idade, 'cidade': cidade}
#imprime o cadastro completo
print('Cadastro')
print(cadastro)
for nome, dados in cadastro.items():
    print('  Nome:', nome)
    print('  Idade:', dados['idade'])
    print('  Cidade:', dados['cidade'])