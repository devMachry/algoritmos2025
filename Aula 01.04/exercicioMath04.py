import math
x = int(input("Digite um valor para X: "))
y = int(input("Digite um valor para y: "))
z = math.floor(  math.sqrt(  (x + math.pow(y,3)) / (math.log10(x)) ) )
print("Resultado de Z:", z)