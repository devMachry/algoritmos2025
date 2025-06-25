# soma = 0
# numero = 1

# while(numero <= 100):
#     soma += numero
#     print(numero)
#     numero += 1

# print("A soma dos números de 1 a 100 é:", soma)

# numero = 50
# while(numero <= 100):
#     if numero % 2 == 0:
#         print(numero)
#     numero += 1



# import random

# pc = random.randint(1,3)
# user = int(input("""\n faça uma jogada entre:===\n1.pedra\n2.papel\n3.tesoura\n===\n\n"""))

# if(user == 1 ):
#     if(pc == 1):
#         print("empate")
#     elif(pc == 2):
#         print("pc ganhou")
#     elif(pc == 3):
#         print("voce venceu")

# elif(user == 2):
#     if(pc == 2):
#         print("empate")

#     elif(pc == 1):
#         print("voce ganhou")
#     elif(pc == 3):
#         print("pc venceu")

# elif(user == 3):
#     if(pc == 3):
#         print("empate")
#     elif(pc == 2):
#         print("voce venceu")
#     elif(pc == 1):
#         print("pc venceu")


# else:
#     print("valor invalido")

# print("inicio do algoritimo")
# cont = 1
# while(cont < 6):
#     print("Valor de cont: ", cont)
#     cont = cont + 1

#     print("Fim do algoritimo")

# entrada = 0
# while(entrada != 3):
#     print("Menu de opções: \n1. Cadastrar \n2. Alterar \3. Sair ")

# numero = int(input("Digite um número de 1 a 10:"))
# print(f"Tabuada do {numero}")
# a = 1

# while(a <= 10):
#     print(f"{numero} x {a} = {numero * a}")
#     a += 1

numero = int(input("Digite um número para ver sua tabuada (1 a 10): "))

print(f"\nTabuada do {numero}:")
i = 1
while(i <= 10):
    print(f"{numero} x {i} = {i * numero}")
    i += 1