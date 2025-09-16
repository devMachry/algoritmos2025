import funcoesCriadas as funcao

totalAlunos = int(input("Digite quantos alunos deseja cadastrar: "))
nomes = [None] * totalAlunos
print(f"Por favor, digite os nomes dos {totalAlunos} alunos.")

contador = 0
while contador < totalAlunos:
    nome_digitado = input(f"Digite o {contador + 1}º nome: ")
    nomes[contador] = nome_digitado
    contador += 1

print("Os nomes digitados foram:", nomes)

notas = [None] * totalAlunos
print(f"Por favor, digite as notas para os {totalAlunos} alunos.")

contador = 0
while contador < totalAlunos:
    nota_digitada = float(input(f"Digite a {contador + 1}ª nota: "))
    notas[contador] = nota_digitada
    contador += 1

print("\nAs notas foram:", notas)


alunos_abaixo = funcao.verificar_notas_abaixo_da_media(notas, nomes)

if alunos_abaixo:
    print("\nAlunos com notas abaixo da média:", alunos_abaixo)
else:
    print("\nNenhum aluno está abaixo da média.")



codigos = ["A001", "A002", "A003"]
quantidades = [10, 5, 8]
precos = [200.0, 150.0, 120.0]


valores_estoque = funcao.calcular_valor_estoque(codigos, quantidades, precos)
print(f"Valores em estoque: {valores_estoque}")



temperaturas = [23.5, 25.0, 28.2, 30.1, 27.3, 22.8, 24.5]
referencia = 25.0
dias_acima = funcao.dias_acima_referencia(temperaturas, referencia)
print(f"Número de dias com temperatura acima de {referencia}°C: {dias_acima}")



salarios = [3000, 2500, 5000, 4000, 3200]
nomes = ["Carlos", "Maria", "Pedro", "Ana", "Luiza"]
print(funcao.salarios_acima_media(salarios, nomes))


vendas = [150, 200, 350, 400, 250, 300]
categorias = ["Eletrônicos", "Roupas", "Eletrônicos", "Móveis", "Roupas", "Eletrônicos"]
print(funcao.total_vendas_por_categoria(vendas, categorias))

# Leia 5 números inteiros e armazene-os em uma lista (vetor).
# Percorra a lista utilizando a estrutura de repetição for.
# Calcule e exiba a soma de todos os números pares contidos na lista.

vetorA = [0] * 5
somaPares = 0
print("-------------------------------------------------------------")
for i in range(0, len(vetorA)):
    vetorA[i] = int(input(f"Digite o {i+1}º número: "))
      
    if(vetorA[i] % 2 == 0):
        somaPares = somaPares + vetorA[i] 

print(f"Seu vetor é:{vetorA}")
 
print("-------------------------------------------------------------") 
        
for i in range(0, len(vetorA)):
        if(vetorA[i] % 2 == 0):
            print(f"Os números pares são: {vetorA[i]}") 
        
print(f"A soma dos pares do seu vetor é: {somaPares}")

print("-------------------------------------------------------------")

for i in range(0, len(vetorA)):
    if(vetorA[i] % 2 != 0):
        print(f"Os números impares do vetor são: {vetorA[i]}")
        
print("-------------------------------------------------------------")

print("\nValores nos indices impares do vetor: ")        
for i in range(0, len(vetorA)):
    if(i % 2 != 0):
        print(f"Indice {i}: {vetorA[i]}")
        
print("-------------------------------------------------------------")
        
print("\nValores nos indices pares do vetor: ")        
for i in range(0, len(vetorA)):
    if(i % 2 == 0):
        print(f"Indice {i}: {vetorA[i]}")

print("-------------------------------------------------------------")        
maior = vetorA[0] 
       
for i in range(0, len(vetorA)):
    if(vetorA[i] > maior):
        maior = vetorA[i]
        
print(f"\nO maior número do vetor é: {maior}")

print("-------------------------------------------------------------")        
menor = vetorA[0] 
       
for i in range(0, len(vetorA)):
    if(vetorA[i] < menor):
        menor = vetorA[i]
        
print(f"\nO menor número do vetor é: {menor}")

import random
def vetAleatorio():
    
    inicial = int(input("Digite um valor inicial para seu vetor: "))
    final = int(input("Digite um valor final para seu vetor: "))
    
    vetAleatorio = [0] * 5
    
    for i in range(0, len(vetAleatorio)):
        vetAleatorio[i] = random.randint(inicial, final)
    
    return vetAleatorio

vetor = vetAleatorio()
print(f"O vetor aleatório é: {vetor}")