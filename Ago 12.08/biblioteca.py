def ola():
    print("Olá, Bem vindo!")
    if(True):
        print("Função Válida!")

def inputInt(msg:str):
    x = input(f"{msg}")
    try:
        x = int(x)
    except:
        print("Valor informado é inválido!")
        x = inputInt(f"{msg}")
    return x

def pedirFloat():
    while(True):
        try:
            x = float(input("Número: "))
            break    
        except:
            print("Float inválido!")
    return x

def somar2(num1:int, num2:int):
    soma = (num1+num2)
    return soma

def somar3(num1:int, num2:int, num3:int):
    soma = (num1+num2+num3)
    return soma

def pot(valor:int, potencia:int):
    resultado = valor**potencia
    return resultado

def raiz(valor:float, grau:int):
    resultado = valor**(1/grau)
    return resultado

def verificaPar(numero:int):
    if(numero % 2 == 0):
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

def ePrimo(x):
    cont = 0
    for i in range(1, x+1):
        if(x % i == 0):
            cont+= 1
    if(cont == 2):
        return True
    else:
        return False
