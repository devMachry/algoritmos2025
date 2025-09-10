import random

vetor = [0] * 8
for i in range(0, len(vetor)):
    vetor[i] = random.randint(0,100)

print(f"Vetor aleatório: {vetor}")

def vetorOrdenado(vetor):
    for i in range(0, len(vetor)-1):
        for cont in range(0, len(vetor)-1):
            if(vetor[cont]<vetor[cont + 1]):
                aux = vetor[cont]
                vetor[cont]=vetor[cont+1]
                vetor[cont + 1] = aux
    return vetor

ordenado = vetorOrdenado(vetor)
print(f"Vetor ordenado {ordenado}")