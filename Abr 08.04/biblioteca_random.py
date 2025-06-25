import random

# v1 = random.randint(1, 10)
# v2 = random.randint(50, 75) 

valor2 = int(input("Informe um valor minimo:"))
valor3 = int(input("Informe um valor máximo:"))
valor = random.randint(valor2, valor3)
print("O valor gerado é: ", valor)
print("O antecessor é: ", valor - 1)
print("O sucessor é: ", valor + 1)
