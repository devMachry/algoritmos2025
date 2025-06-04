import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = math.pow(b, 2) - 4*a*c

if delta < 0:
    print("Não existem raízes reais.")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(f"Raízes: {x1:.2f} e {x2:.2f}")