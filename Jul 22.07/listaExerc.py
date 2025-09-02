numeros = [0] * 100

for i in range(0, len(numeros)):
    numeros[i] = i + 1
for i in range(0, len(numeros)):
    print(f"Numero: {numeros[i]:03d}", end=" ")

for i in range(len(numeros)-1,-1,-1):
    numeros[i] = i - 1
for i in range(len(numeros)-1,-1, -1):
    print(f"Numero: {numeros[i]}")
