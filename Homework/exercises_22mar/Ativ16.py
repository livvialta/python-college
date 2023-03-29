nums = [input("Insira um numero: "),input("Insira um numero: "),input("Insira um numero: "),input("Insira um numero: "),input("Insira um numero: "),input("Insira um numero: "),input("Insira um numero: ")]
 
duplicados = [x for i, x in enumerate(nums) if i != nums.index(x)]
print(duplicados) 
    

