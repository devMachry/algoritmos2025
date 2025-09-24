# 1. Criar uma biblioteca com 5 funções que:
# recebe um vetor e retorna ele ordenado pelo algoritmo de bolha
# recebe um vetor e retorna ele ordenado pelo algoritmo de inserção
# recebe um vetor e retorna ele ordenado pelo algoritmo de seleção
# recebe um vetor e um número (valor) e retorna o índice daquele valor no vetor usando a busca sequencial ou retorna -1 se não 
# tiver o valor.
# recebe um vetor e um número (valor) e retorna o índice daquele valor no vetor usando a busca binária ou retorna -1 se 
# não tiver o valor

def bolha(vetor):
    for ciclo in range(0, len(vetor)-1):
        for i in range(0, len(vetor)-1):
            if(vetor[i] > vetor[i+1]):
                copia = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = copia
    return vetor


def insercao(vetor):
    for i in range(1,len(vetor)):
        temp = vetor[i]
        j = i - 1
        while( j >= 0 and temp < vetor[j]):
            vetor[j+1] = vetor[j]
            j = j - 1

        vetor[j + 1] = temp
    return vetor
    


def selecao(array):
    for i in range(0, len(array) -1):
        menor = array[i]
        imenor = i
        for j in range(i+1, len(array)):
            if(array[j] < menor):
                menor = array[j]
                imenor = j

        array[imenor] = array[i]
        array[i] = menor
            
    return array

def busca_sequencial_nao_ordenada(array, valor):
    indice = None
    for i in range(0, len(array)):
        if(valor == array[i]):
            indice = i
            break

    return indice

def busca_sequencial_ordenada(array,valor):
    array = insercao(array)
    indice = None
    for i in range(0, len(array)):
        if(valor < array[i]):
            indice = i
            break

    return indice

def busca_binaria(array, valor):
    indice = None
    inicio = 0
    fim = len(array) - 1
    
    while(inicio <= fim):
        meio = int((inicio + fim) / 2)

        if(array[meio] == valor):
            indice = meio
            break
        elif(array[meio] > valor):
            fim = meio - 1
        else:
            inicio = meio + 1

    return indice