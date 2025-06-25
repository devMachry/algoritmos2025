# for i in range(10, -1, -1):
#     print(i)

# tabuada = int(input("Digite um número para a tabuada: "))

# for i in range(1, 11):
#     resultado = tabuada * i
    # print(f"{tabuada} x {i} = {resultado}")

tabuada = int(input("Digite um numero para a tubuada: " ))
num1 = int(input("Digite um numero inicial: " ))
num2 = int(input("Digite um numero final: " ))

for i in range(num1, num2 + 1):
    print(f"{tabuada} x {i} = {tabuada*i}")