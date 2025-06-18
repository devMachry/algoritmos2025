import random
# for i in range(1, 101):
#     print(i)


# for i in range(100, 0, -1):
#     print(i)


# for i in range(0, 100, 2):
#     print(i)


# for i in range(1, 6):
#     numero = int(input("Digite um número: "))

# x = 0
# for i in range(0, 5):
#     x = random.randint(1, 100)
#     print(x)


x = 0
num1 = int(input("Dígite um valor mín: "))
num2 = int(input("Digite um valor máx: "))
quantidade = int(input("Digite quantos numeros deseja sortear: "))

if(num1 > num2):
    num3 = num1
    num1 = num2
    num2 = num3

soma = 0
maior = max
menor = min
for i in range(0, quantidade):
    x = random.randint(num1, num2)

    soma += x
    if(x > maior):
        maior = x

    if(x < menor):
        menor = x



print("------- Relatório do programa ---------")
print(f"A soma dos números é: {soma}")


