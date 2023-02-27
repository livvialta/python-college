print("Meu\nnome\né\nLívia.")

# \n - é o comando para pular linha.

print("Meu\nnome\né\nLívia",end= "123")

end = juntar na ultima palavra que voce escreveu.

print("Lívinha Oreiuda.")

print("peixe", "chips", sep="&")

sep = "(alguma coisa)" # vai separar os dois elementos.

print("2")
print(2) 
print(0x123) #Número hexadecimal para binário.

print(0.0000000000000000000001)
print("Eu gosto \"Monty Python\"") 

#\’\’ utilizado para quando você quer usar uma aspas simples (ou duplas) enquanto dentro de uma aspas simples (ou duplas).

#Mais alguns exemplos de usos de aspas:
print('I like "Monty Python"') 
print('I\'m Monty Python.')

#----------------------------------------------------------------------------------------------------------------------------------

#Operadores

print(14 % 4) #Resto da multiplicação de 14/4
print(5 % 5) #Resto da multiplicação de 5/5
print(10 % 1) #Resto da multiplicação de 10/1
print(9 % 6 % 2) #Resto da multiplicação 
print(2 ** 2 ** 3) #Potenciação, começa da esquerda para direita a ordem da resolução (A potenciação é a única que começa da esquerda para direita)
print(2 * 3 % 5) #Divisão e resto da divisão.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) #Conta com várias operações.
print((2 ** 4), (2 * 4.), (2 * 4)) #Conta com várias operações.
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # Conta com várias operações.
print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # Conta com várias operações.


#---------------------------------------------------------------------------------------------------------------------------------------

#Desafio do professor

a=  float(input("Insira um valor para A: \n "))
b=  float(input("Insira um valor para B: \n"))
c=  float(input("Insira um valor para C: \n"))

if a > b and a > c:
    print("O número A é o maior número.")

elif b > a and b > c: 
    print("O número B é o maior número.")

else:
    print("O número C é o maior número.")

#---------------------------------------------------------------------------------------------------------------------------------------

var= "3.10.5"

print("Versão do Python:", var)

#---------------------------------------------------------------------------------------------------------------------------------------


#Criando váriaveis

kilometros = float(input("Entre com o valor de Kilometros: \n"))
milhas = float(input("Ente com o valor de milhas: \n"))

#Executar operações
milhas_kilometros = milhas * 1,61
kilometros_milhas = kilometros / 1,61

print(milhas, " equivalente a" round(milhas_kilometros,2), "kilometros.")
print(kilometros,"equivalente a", round(kilometros_milhas,2), "milhas.")

#---------------------------------------------------------------------------------------------------------------------------------------

x = input("Entre com um número: ") 
print(type(x)) - esse comando serve para entender qual valor estamos trabalhando, se é string, float, int, etc.

#---------------------------------------------------------------------------------------------------------------------------------------
