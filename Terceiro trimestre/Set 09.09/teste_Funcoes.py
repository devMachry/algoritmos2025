import biblioteca_Funcoes as bib
import random

vetor = [0] * 5
for i in range(0,len(vetor)):
    vetor[i] = random.randint(0,50)

print(f" O vetor gerado foi: {vetor}")
ordenaBolha = bib.bolha(vetor)

print(f"Vetor ordenado pelo método bolha: {ordenaBolha}")


vetorA = [0] * 10
for i in range(0,len(vetorA)):
    vetorA[i] = random.randint(0,70)

print(f" O vetor gerado foi: {vetorA}")

ordenaInsercao = bib.insercao(vetorA)

print(f"Vetor ordenado pelo método inserção: {ordenaInsercao}")

vetorB = [0] * 10
for i in range(0,len(vetorB)):
    vetorB[i] = random.randint(20,80)

print(f" O vetor gerado foi: {vetorB}")

ordenaSelecao = bib.selecao(vetorB)

print(f"Vetor ordenado pelo método seleção: {vetorB}")
