"""
1. Crie um programa que abra (ou crie) um arquivo chamado frutas.txt e escreva nele 5 nomes de frutas, um em cada linha.
Use o modo de abertura w.

arquivo = "frutas.txt"

arq = open(arquivo, "w", encoding="utf8")

arq.write("Maçã\n")
arq.write("Morango\n")
arq.write("Melancia\n")
arq.write("Laranja\n")
arq.write("Pera\n")

arq.close()

2. Crie um programa que leia o conteúdo do arquivo frutas.txt e mostre cada fruta precedida da frase:
 "Eu adoro a fruta: <fruta>"

arq = open("frutas.txt", "r", encoding="utf8")

conteudo = arq.readlines()

arq.close()

for i in range(0, len(conteudo)):
    print(f"Eu adoro a fruta: {conteudo[i]}")

3. Agora abra o arquivo frutas.txt no modo a e adicione mais 3 frutas. Depois, leia e exiba todo o conteúdo novamente.
arquivo = "frutas.txt"

arq = open(arquivo, "a", encoding="utf8")

arq.write("Mamão\n")
arq.write("Melão\n")
arq.write("Banana\n")

arq.close()


4. Crie um programa que apague todo o conteúdo do arquivo frutas.txt (dica: modo w sem escrever nada) e escreva 
apenas: "Desculpe, esqueci tudo 😅"

arquivo = "frutas.txt"

arq = open(arquivo, "w", encoding="utf8")

arq.write("Desculpe, esqueci tudo 😅\n")


arq.close()

"""
'''
5. Lista de compras interativa
Peça para o usuário digitar 5 itens de compra e escreva cada um em uma nova linha no arquivo compras.txt.

arquivo = "compras.txt"
arq = open(arquivo, "w", encoding="utf8")

minhaCompra = [0] * 5 

for i in range(0,len(minhaCompra)):
    minhaCompra[i] = input(f"Digite o item {i+1}:")

for i in range(0, len(minhaCompra)):
    arq.write(f"{minhaCompra[i]}\n")

arq.close()

arq = open("compras.txt", "r", encoding="utf8")

minhaCompra = arq.readlines()

arq.close()

for i in range(0, len(minhaCompra)):
    print(f"{i+1} - {minhaCompra[i]}")

'''
'''
EXERCICIO 8

arq = open("notas.txt", "r")

conteudo = arq.readlines()
soma = 0
nomeMaior = " "
maior = 0

for i in range(0, len(conteudo)):
    linha = conteudo[i]
    valores = linha.split(",")
    soma += float(valores[1])  #soma os valores na posição 1 do vetor

    if(float(valores[1]) > maior):
        maior = float(valores[1])
        nomeMaior = valores[0]

    if(float(valores[1]) < 8):
        print(f"{valores[0]} tirou menos que 8")


media = soma/ len(conteudo)
print("Média dos valores", media)
print(f"{nomeMaior} tem maior nota {maior}")
'''

'''
EXERCICIO 9

arq = open("compras.txt", "r")

conteudo = arq.readlines()

arq.close()

#Pede o nome do cliente que será pesquisado

nomeCliente = input("Digite o nome do cliente que deseja buscar: ")

total = 0 

for i in range(0, len(conteudo)):
    linha = conteudo[i]             #pega uma linha do arquivo
    valores = linha.split(",")      #separa o nome e o valor
    nome = valores[0]
    valor = float(valores[1])

if(nome == nomeCliente):
    total = total + valor

print(f"{nomeCliente} - Total: R${total:.2f}")

'''


# arquivo = "vendas.txt"

# arq = open(arquivo, "w", encoding="utf8")

# arq.write("2025-09-28,Joana,120.00\n")
# arq.write("2025-09-29,Tiago,75.00\n")
# arq.write("2025-09-29,Joana,80.00\n")
# arq.write("2025-09-30,Pedro,100.00\n")

# arq.close()



arq = open("vendas.txt", "r")

conteudo = arq.readlines()

arq.close()

dataBusca =  input("Digite a data (AAAA-MM-DD): ")
total = 0
vendeu = False
 
for i in range(0, len(conteudo)):
    linha = conteudo[i]
    valores = linha.split(",")

    data = valores[0]
    nome = valores[1]
    valor = float(valores[2])

if(data == dataBusca):
    vendeu = True
    print(f"{nome} vendeu R${valor:.2f}")
    total = total + valor

if(vendeu):
     print(f"Total vendido em {dataBusca}: R${total:.2f}")
else:
    print("Nenhuma venda encontrada nessa data.")


