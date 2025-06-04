import random
#Exercicio 01

# numero = int(input("Digite um número: "))

# if(numero >= 0):
#     print("O valor digitado é positivo!")

# else:
#     print("O valor é negativo!")

#Exercicio 02

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# if(num1 > num2):
#     print(num1)

# else:
#     print(num2)

# Exercicio 03 
# idade = int(input("Digite sua idade: "))

# if(idade >= 18):
#     print("Você é de maior! Entrada permitida!")

# else:
#     print("Você é menor de idade!Entrada negada!")

#Exercicio 04

# trabalho = int(input("Digite a nota do trabalho de 0 a 100: "))
# prova = int(input("Digite a nota da prova de 0 a 100: "))

# media = (trabalho + prova)/2

# if(media >= 60):
#     print("Aprovado!")

# else:
#     print("Reprovado!")

#Exercicio 5

# salarioRecebido = float(input("Informe o seu salário: "))
# salarioMinimo = 1212.00
# totalDeSalario = salarioRecebido/salarioMinimo

# if(salarioRecebido > salarioMinimo):
#     print(f"Voce recebe {totalDeSalario} salários mínimo")

# else:
#     print("Você recebe menos de um salário mínimo!")

#Exercicio 6

# sexo = str(input("Informe seu sexo. Ex: F para Feminino e M para Masculino: ")).upper()

# if(sexo == "F"):
#     print("Feminino")

# else:
#     print("Masculino")

# Exercicio 7

# idade = int(input("Digite sua idade: "))

# if(idade >= 18):
#     nome = input("Digite o seu nome: ")
#     print(f"Bem vindo {nome}")

# else:
#     print("Entrada não permitida!")

# Exercicio 8

# idade = int(input("Digite a sua idade: "))

# if(idade >= 18):
#     salario = float(input("Digite os seu salário: "))
#     salAumento = salario + (salario * 0.05)
#     print("O valor final do seu salário com aumento é: ", salAumento)
# else:
#     print("Você é de menor!")
#     print("Cálculo não permitido!")

# Exercicio 9

# numero = int(input("Digite um número inteiro: "))

# if(numero >= 0 |numero <= 100):
#     print("Número no intervalo definido")

# else:
#     print("Número fora do intervalo!")

# Exercicio 10

# num = int(input("Digite um número: "))

# if(num % 2 == 0):
#     print("Par")
# else:
#     print("Impar")

# Exercicio 11

# numero = int(input("Digite um número: "))

# if numero % 3 == 0:
#     print(f"{numero} é múltiplo de 3")
# else:
#     print(f"{numero} não é múltiplo de 3")

# Exercicio 12

# numAleatorio = random.randint(1, 10)
# numero = int(input("Digite um número: "))

# if(numAleatorio == numero):
#     print("Acertou o número aleatório!")

# else:
#     print("Errou o número aleatório!")

# Exercicio 13

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# num3 = int(input("Digite um número entre os valores digitados antes: "))

# aleatorio = random.randint(num1, num2)

# if(aleatorio == num3):
#     print("Acertou o número aleatório!")

# else:
#     print("Errou o número aleatório!")

# Exercicio 14

# a = int(input("Digite um valor para A: "))
# b = int(input("Digite um valor para B: "))
# c = int(input("Digite um valor para C: "))

# if((a+b)>c):
#     print("A+B é maior que C")

# else:
#     print("C é maior que todos!")

# Exercicio 15

# numero = int(input("Digite um número inteiro: "))

# if(numero % 2 == 0):
#     numPar = numero + 5
#     print(numPar)

# else:
#     numImpar = numero * 2
#     print(numImpar)

# Exercicio 16

# numero1 = float(input("Digite um número: "))

# if(numero1 < 0):
#     numero2 = float(input("Digite outro número"))

# if(numero1 > 0):
#     print(numero1 * 10)
# else:
#     print(numero2 * 10)

# Exercicio 17

# numero = int(input("Digite um número: "))

# if(numero % 2 == 0):
#     print("O número é par!")
# else:
#     print("Número ímpar!")

# if(numero < 0):
#     print(numero + 100)

# Exercicio 18

# desconto = 0.1
# compra = float(input("Digite o valor da sua compra: "))

# if(compra > 100):
#     totalDesc = ((compra) * (desconto))
#     print(f"O valor do desconto é: {totalDesc}")
#     print(f"O valor final é:{compra - totalDesc}")
# else:
#     print(f"Preço total: {compra}")

# Exercicio 19

# salario = float(input("Digite o salário bruto: R$ "))

# if salario <= 1903.98:
#     imposto = 0
#     print("Isento de imposto de renda")

# elif salario <= 2826.65:
#     imposto = salario * 0.075
#     print(f"Valor do imposto(7,5%): R$ {imposto}")
# else:
#     imposto = salario * 0.15
#     print(f"Valor do imposto(15%): R$ {imposto}")

#Exercicio 20

# valorCompra = float(input("Digite o valor da compra: R$ "))
# formaPagamento = input("Digite a forma de pagamento (PIX, cartão, dinheiro): ").upper()

# if valorCompra > 500:
#     if formaPagamento == "PIX":
#         desconto = valorCompra * 0.10
#     else:
#         desconto = valorCompra * 0.05
# else:
#     if formaPagamento == "PIX":
#         desconto = valorCompra * 0.05
#     else:
#         desconto = 0

# valorFinal = valorCompra - desconto

# print(f"O valor final é: R$ {valorFinal}")

# Exercicio 21

# x = int(input("Digite um valor para X: "))
# fx = 0

# if(x < 2):
#     fx = 1 / (2-x)
# else:
#     if(x == 2):
#         fx = 0
    
#     else:
#         fx = 1 / (x-2)

# print(f"O resultado de x é: {fx}")