# Ordenação de vetor do tipo bolha

def matematica(x):
    x=5

x = 10
print(x)
matematica(x) # envia o valor 10 para a função e não o x
print(x)
exit()


def bolha(vetor):
    for ciclo in range(0, len(vetor)-1):
        for i in range(0, len(vetor)-1):
            if(vetor[i] > vetor[i+1]):
                copia = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = copia

vet = [10,9,8,7,6,7,8]

print(vet)
# envia o vetor por referencia, ou seja, envia o original.
bolha(vet)
print(vet)

def insercao(vetor):
    for i in range(1,len(vetor)):
        temp = vetor[i]
        j = i - 1
        while( j <= 0 and temp < vetor[j]):
            vetor[j+1] = vetor[j]
            j = j - 1

        vetor[j] = temp


# ordenação por seleção

def selecao(vetor):
    for i in range(0, len(vetor)):
        
