import revisao as rev
import random

def vetorAleatorio(tamanho_min=5, tamanho_max=10):
    tamanho = random.randint(tamanho_min, tamanho_max)
    return [random.randint(1, 100) for i in range(tamanho)]

while (True):
    print("\n--- MENU DE FUNÇÕES ---")
    print("1. Calcular a Média")
    print("2. Verificar se a soma é Par ou Ímpar")
    print("3. Encontrar o Maior número em um vetor")
    print("4. Somar números em posições pares de um vetor")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Números aleatórios gerados: {num1} e {num2}")
        resultadoMedia = rev.media(num1, num2)
        print(f"A média é: {resultadoMedia}")

    elif opcao == '2':
        soma = rev.verificarResultado()

    elif opcao == '3':
        vetor = vetorAleatorio()
        print(f"Vetor gerado: {vetor}")
        maiorNumero = rev.verificarMaior(vetor)
        print(f"O maior número no vetor é: {maiorNumero}")

    elif opcao == '4':
        vetor = vetorAleatorio()
        soma = rev.somarNumeros(vetor)
        print(f"A soma do vetor é: {soma}\n")

    elif opcao == '5':
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")