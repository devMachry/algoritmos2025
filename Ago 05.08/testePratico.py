# precosFrutas = [0.0] * 6

# for i in range(0, len(precosFrutas)):
#     msg = f"Fruta {i+1} R$ "
#     precosFrutas[i] = float(input(msg))

# for i in range(0, len(precosFrutas)):
#     print(f"Preço da fruta {i + 1}: R$ {precosFrutas[i]:.2f}")


import random

temperatura = [0.0] * 24

for i in range(0, len(temperatura)):
    temperatura[i] = random.randint(15, 30)


for i in range(0, len(temperatura)):
    print(f"Temperatura {i + 1}: {temperatura[i]}")

somaTemperatura = 0
for i in range(0, len(temperatura)):
    somaTemperatura += temperatura[i]

temperaturaMedia = somaTemperatura / temperatura[i]
print(f"A média de temperatura é: {temperaturaMedia:.2f}")

maiorTemperatura = temperatura[0]
horaMaiorTemperatura = 0

for i in range(0, len(temperatura)):
    if temperatura[i] > maiorTemperatura:
        maiorTemperatura = temperatura[i]
        horaMaiorTemperatura = i

print(f"A maior temperatura registrada foi {maiorTemperatura}°C, às {horaMaiorTemperatura} h.")

contarMaiorTemperatura = 0
for i in range(0, len(temperatura)):
    if temperatura[i] == maiorTemperatura:
        contarMaiorTemperatura += 1

print(f"A maior temperatura apareceu {contarMaiorTemperatura} vez(es).")

horarios = [0] * contarMaiorTemperatura
controle = 0
for i in range(0, len(temperatura)):
    if(maiorTemperatura == temperatura[i]):
        horarios[controle] = i
        controle += 1

for i in range(0, len(horarios)):
    print(f"Horarios de maior temperatura: {horarios[i]}h.")