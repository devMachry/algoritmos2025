
def media(a, b):
    soma = (a+b)
    media = soma/2
    return media

def verificarResultado(n1, n2):
    soma = (n1+n2)
    if(soma % 2 == 0):
        print(f"A soma de {n1} e {n2} é {soma} e é PAR!")
    else:
        print(f"A soma de {n1} e {n2} é {soma} e é ÍMPAR!")

def verificarMaior(vetor):
    for i in range(0, len(vetor)):
        if(i == 0):
            maior = vetor[i]
        if(vetor[i] > maior):
            maior = vetor[i]
    return maior


def somarNumeros(vetor):
  soma = 0
  for i in range(len(vetor)):
    if(i % 2 == 0):
      soma += vetor[i]
  return soma

