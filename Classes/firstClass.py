initial_v = int(input("Entre com a velocidade inicial:"))
aceleration =int(input("Agora, entre com a aceleração:"))
time=int(input("E por fim, qual foi o tempo?"))

print("Velocidade é igual a =", initial_v + aceleration * time)

#----------------------------------------------------------------------------------------------------------
#Insert the data
initialPosition = float(input("Entre com a posição inicial:"))
velocity =float(input("Agora, entre com a velocidade inicial:"))
time=float(input("E por fim, o intervalo de tempo?"))
aceleration = float(input("Entre com a aceleração:"))

s= initialPosition + velocity * time + (aceleration * (time **2)//2)

print("A posição final é igual a =", s)

#----------------------------------------------------------------------------------------------------------

s = float(input("Entre com a posição inicial:"))
so = float(input("Entre com a posição final:"))
t = float(input("Entre com o tempo inicial:"))
to = float(input("Entre com o tempo final:"))

if (t == to):
    print ("Erro! Entre com valores diferentes.")
else:
    print ("A velocidade é igual a", ( (s - so)// (t - to)))



