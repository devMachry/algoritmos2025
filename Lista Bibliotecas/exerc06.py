import random

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

sorteado = random.randint(num1, num2)

print(f"\nNúmeros inseridos: {num1} e {num2}")
print(f"Número sorteado: {sorteado}")