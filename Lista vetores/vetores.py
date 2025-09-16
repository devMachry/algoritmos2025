# Exercício 01: Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista)
# vetorA = [0] * 100

# for i in range(0, len(vetorA)):
#     vetorA[i] = i + 1
    
# print(vetorA)

# A) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).

# for i in range(0, len(vetorA)):
#     print(f"Vetor ordem crescente: {vetorA[i]} ")
    
# b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).

# for i in range(99, -1, -1):
#     print(vetorA[i])
    
# C) Mostre na tela o dobro de todos os números.

# for i in range(0, len(vetorA)):
#     vetorA[i] = (i + 1) * 2
    
#     print(vetorA[i])

# D) Apresente na tela a soma de todos os números.
# soma = 0
# for i in range(0, len(vetorA)):
#     vetorA[i] = i + 1
#     soma += vetorA[i]
    
# print(f"A soma de todos os numeros do vetor é: {soma}")

# F) Apresente na tela a média geral dos valores contidos na lista.

# soma = 0
# for i in range(0, len(vetorA)):
#     vetorA[i] = i + 1
#     soma += vetorA[i]
    
# media = soma/len(vetorA)

# print(f"A média de todos os numeros do vetor é: {media}")

# G) Mostre na tela a quantidade de números pares.
# contaPares = 0

# for i in range(0, len(vetorA)):
#     if(vetorA[i] % 2 == 0):
#         contaPares += 1
        
# print(f"A quantidade de numeros pares no vetor é: {contaPares}")

# Exercício 2: Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso.
# Faça um programa para armazenar 5 nomes e permitir que o professor digite o nome de cada um.
# Em seguida, apresente na tela todos os nomes informados.

# listaAlunos = [""] * 5

# for i in range(0, len(listaAlunos)):
#     listaAlunos[i] = input(f"Digite o nome do {i + 1}º aluno: ")

# print(f" Os alunos são: {listaAlunos}")

# Exercício 3: Faça um programa que peça para o usuário informar o tamanho de um vetor.
# Em seguida, crie este vetor e preencha ele com números digitados pelo usuário.
# Por fim, apresente na tela os números digitados.

tamVetor = int(input("Qual o tamanho desejado para seu vetor: "))
print(f"Seu vetor terá {tamVetor} números!")
vetorUsuario = [0] * tamVetor

for i in range(0, len(vetorUsuario)):
    vetorUsuario[i] = int(input(f"Digite o {i + 1}º numero para seu vetor: "))
    
print(f"Os numeros do seu vetor são: {vetorUsuario}")

# A) Vetor na ordem inversa
# vetorInverso = [0] * tamVetor

# for i in range(tamVetor):
#     vetorInverso[i] = vetorUsuario[tamVetor - 1 - i ]
    
# print(f"Os números do vetor em ordem inversa são: {vetorInverso}") 

# B) Soma dos elementos e média aritmética
# soma = 0
# for i in range(0, len(vetorUsuario)):
#     vetorUsuario[i] = i+1
#     soma += vetorUsuario[i]
    
# media = soma/tamVetor

# print(f"A soma dos elementos é: {soma} ")
# print(f"A média dos elementos é: {media} ")

# C) Liste na tela somente os números do vetor que estão em posições (índices) pares.
# for i in range(0, tamVetor, 2):
#     print(f"Posiçao {i}: {vetorUsuario[i]}")

posInicial = int(input("\nInforme a posição inicial do segmento: "))
posFinal = int(input("Informe a posição final do segmento: "))

if(posInicial < 0 or posFinal >= tamVetor or posInicial > posFinal):
    print("Posições inválidas! Certifique-se de que:")
    print("- A posição inicial não é negativa")
    print("- A posição final está dentro do tamanho do vetor")
    print("- A posição inicial vem antes ou é igual à final")
else:
    print("\nSegmento selecionado:")
    for i in range(posInicial, posFinal + 1):
        print(vetorUsuario[i])