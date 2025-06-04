import math

angulo = float(input("Digite o ângulo em graus: "))
radianos = math.radians(angulo)

print(f"Seno: {math.sin(radianos):.3f}")
print(f"Cosseno: {math.cos(radianos):.3f}")
print(f"Tangente: {math.tan(radianos):.3f}")