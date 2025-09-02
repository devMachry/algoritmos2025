import biblioteca as bib
import random
# bib.ola()

# num = bib.inputInt("Digite um número: ")
# num2 = bib.inputInt("Digite outro número: ")

# soma = bib.somar2(num,num2)
# potencia = bib.pot(num,num2)
# raiz = bib.raiz(num,num2)
# print(f" A potência é: {potencia}")
# print(f" A raiz é: {raiz:.2f}")
# print(f"A soma de dois valores é: {soma}")

# valor1 = bib.inputInt("Digite um número: ")
# valor2= bib.inputInt("Digite outro número: ")
# valor3= bib.inputInt("Digite mais um número: ")

# calcular = bib.somar3(valor1,valor2,valor3)
# print(f"A soma de três valores é:{calcular}")

# verificaPar = bib.inputInt("Digite um número: ")
# par = bib.verificaPar(verificaPar)


for i in range(1, 101):
    verificaPrimo = bib.ePrimo(i)
    if(verificaPrimo):
        print(f"{i} é primo")



