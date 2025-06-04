import time

segundos = int(input("Digite o tempo em segundos: "))

print("Preparar, apontar, vai...")
time.sleep(segundos)
print(f"Tempo esgotado! Foram {segundos} segundos.")