
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

def calcular_valor_estoque(codigos, quantidades, precos):
    
    valores_estoque = [0] * len(codigos)
    
   
    for i in range(len(codigos)):
        valores_estoque[i] = quantidades[i] * precos[i]
    
    return valores_estoque


def verificar_notas_abaixo_da_media(notas, nomes):
    total_notas = 0  

    for nota in notas:
        total_notas += nota
    
    media = total_notas / len(notas)
    
    alunos_abaixo_da_media = []
    
    for i in range(len(notas)):
        if notas[i] < media:
            alunos_abaixo_da_media = alunos_abaixo_da_media + [nomes[i]]
    
    return alunos_abaixo_da_media

def dias_acima_referencia(temperaturas, referencia):

    contador = 0
    
    for temperatura in temperaturas:
        if temperatura > referencia:
            contador += 1
    return contador

def salarios_acima_media(salarios, nomes):
    totalSalarios = 0
    
    for salario in salarios:
        totalSalarios += salario
        
    mediaSalarios = totalSalarios/ len(salarios)
    
    salariosAcimaMedia = []
    
    for i in range(len(salarios)):
        if salarios[i] > mediaSalarios:
            salariosAcimaMedia = salariosAcimaMedia + [nomes[i]]
            
    return salariosAcimaMedia

def total_vendas_por_categoria(vendas, categorias):
    total_por_categoria = {}
    
    for i in range(len(vendas)):
        categoria = categorias[i]  
        venda = vendas[i]          
        
        if categoria in total_por_categoria:
            total_por_categoria[categoria] += venda
        else:
        
            total_por_categoria[categoria] = venda
    
    return total_por_categoria
