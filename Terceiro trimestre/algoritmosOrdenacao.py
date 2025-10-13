def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if(lista[i] > lista[i+1]):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        temp = lista[i]
        j = i - 1
        while(j >= 0 and lista[j] > temp):
            lista[j+1] = lista[i]
            j = j - 1
        lista[j+1] = temp

def selection_sort(lista):
    n = len(lista)
    for i in range(0, n -1):
            minimo = lista[i]
            imenor = i
            for j in range(i+1, n):
                if lista[j] < minimo:
                    menor = lista[j]
                    imenor = j
            lista[imenor] = lista[i]
            lista = menor
    return lista

def buscaSequencial(vetor, valor):
    posicao = -1

    for i in range(0, len(vetor)):
        if(vetor[i] == valor):
            posicao = i
            break

    return posicao

def busca_binaria(vetor, valor):
    inicio = 0                  # primeira posição do vetor
    fim = len(vetor) - 1        # última posição do vetor
    posicao = -1                # começa como não encontrado

    while inicio <= fim:
        meio = (inicio + fim) // 2  # calcula o índice do meio

        if vetor[meio] == valor:
            posicao = meio          # achou o valor
            break                   # sai do laço

        elif valor < vetor[meio]:
            fim = meio - 1          # busca fica na metade da esquerda

        else:
            inicio = meio + 1       # busca fica na metade da direita

    return posicao  # devolve o índice ou -1

