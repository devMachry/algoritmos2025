import random

numero = random.randint(1, 100)

print(f"Número sorteado: {numero}")
print("Par" if numero % 2 == 0 else "Ímpar")
print("Múltiplo de 5" if numero % 5 == 0 else "Não é múltiplo de 5")