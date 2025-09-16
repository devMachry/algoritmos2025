import random

# Exercicio 1: Programa principal com menu
def exibir_menu():
    print("\nEscolha uma opção:")
    print("1 - Pedir um número inteiro")
    print("2 - Gerar número aleatório")
    print("3 - Sortear números aleatórios")
    print("4 - Converter número para mês")
    print("5 - Calcular áreas")
    print("6 - Calcular fatorial")
    print("7 - Encontrar maior valor de um vetor")
    print("8 - Encontrar menor valor de um vetor")
    print("9 - Calcular média de um vetor")
    print("10 - Dobrar os valores de um vetor")
    print("11 - Converter data para o formato por extenso")
    print("12 - Sair")

# Função para pedir um número inteiro
def numero_inteiro():
    numero = int(input("Digite um número inteiro: "))
    print(f"O número digitado foi: {numero}")

# Função para gerar número aleatório
def gerar_numero_aleatorio():
    n = int(input("Digite um número para definir o intervalo (1 a n): "))
    numero_aleatorio = random.randint(1, n)
    print(f"O número aleatório gerado foi: {numero_aleatorio}")

# Funções para sortear números aleatórios
def sortear_numero_intervalo():
    limite_inferior = int(input("Digite o limite inferior: "))
    limite_superior = int(input("Digite o limite superior: "))
    numero = random.randint(limite_inferior, limite_superior)
    print(f"Número sorteado: {numero}")

def sortear_numero_impar():
    numero_impar = random.choice([x for x in range(1, 100, 2)])
    print(f"Número ímpar sorteado: {numero_impar}")

# Função para converter número em mês
def numero_para_mes():
    numero = int(input("Digite um número de 1 a 12: "))
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    if 1 <= numero <= 12:
        print(f"O mês correspondente é: {meses[numero]}")
    else:
        print("Mês inválido!")

# Funções para resolver as equações de área
def calcular_area():
    print("Escolha a figura para calcular a área:")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Triângulo")
    print("4 - Trapézio")
    escolha = int(input("Digite a opção: "))
    
    if escolha == 1:
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print(f"A área do quadrado é: {area}")
    elif escolha == 2:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print(f"A área do retângulo é: {area}")
    elif escolha == 3:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print(f"A área do triângulo é: {area}")
    elif escolha == 4:
        base_maior = float(input("Digite a base maior do trapézio: "))
        base_menor = float(input("Digite a base menor do trapézio: "))
        altura = float(input("Digite a altura do trapézio: "))
        area = ((base_maior + base_menor) * altura) / 2
        print(f"A área do trapézio é: {area}")
    else:
        print("Opção inválida!")

# Exercicio 7: Função para calcular o fatorial de um número
def fatorial(n):
    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 1
    return resultado

# Funções para vetor (maior valor, menor valor, média, dobrar)
def maior_valor(vetor):
    maior = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior

def menor_valor(vetor):
    menor = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor

def media_vetor(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
    media = soma / len(vetor)
    return media

def dobro_vetor(vetor):
    resultado = [0] * len(vetor)  # cria um vetor do mesmo tamanho
    for i in range(len(vetor)):
        resultado[i] = vetor[i] * 2
    return resultado

# Função para converter data no formato por extenso
def data_por_extenso(data):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    partes = data.split('/')  # separa DD, MM, AAAA
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    if 1 <= mes <= 12:
        nome_mes = meses[mes - 1]
        return f"{dia} de {nome_mes} de {ano}"
    else:
        return "Data inválida"

# Função para inserir um vetor de números manualmente
def obter_vetor():
    vetor = []
    tamanho = int(input("Quantos números você quer inserir no vetor? "))
    for i in range(tamanho):
        numero = int(input(f"Digite o {i + 1}º número: "))
        vetor.append(numero)
    return vetor

# Função principal que executa o menu
def main():
    while True:
        exibir_menu()
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            numero_inteiro()
        
        elif opcao == 2:
            gerar_numero_aleatorio()
        
        elif opcao == 3:
            print("Escolha a função de sorteio:")
            print("1 - Sortear número em intervalo")
            print("2 - Sortear número ímpar")
            sorteio = int(input("Digite a opção: "))
            if sorteio == 1:
                sortear_numero_intervalo()
            elif sorteio == 2:
                sortear_numero_impar()
            else:
                print("Opção inválida!")
        
        elif opcao == 4:
            numero_para_mes()
        
        elif opcao == 5:
            calcular_area()
        
        elif opcao == 6:
            numero = int(input("Digite um número para calcular o fatorial: "))
            print(f"O fatorial de {numero} é: {fatorial(numero)}")
        
        elif opcao == 7:
            vetor = obter_vetor()
            print(f"O maior valor do vetor é: {maior_valor(vetor)}")
        
        elif opcao == 8:
            vetor = obter_vetor()
            print(f"O menor valor do vetor é: {menor_valor(vetor)}")
        
        elif opcao == 9:
            vetor = obter_vetor()
            print(f"A média dos valores do vetor é: {media_vetor(vetor)}")
        
        elif opcao == 10:
            vetor = obter_vetor()
            print(f"O vetor com os valores dobrados é: {dobro_vetor(vetor)}")
        
        elif opcao == 11:
            data = input("Digite a data no formato DD/MM/AAAA: ")
            print(f"A data por extenso é: {data_por_extenso(data)}")
        
        elif opcao == 12:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, por favor tente novamente!")

# Inicia o programa
main()