resposta = input("O ar-condicionado está ligado? (Digite 'True' ou 'False'): ")

if resposta.lower() == 'true':
    ar_ligado = True
else:
    ar_ligado = False

if ar_ligado:
    print("Ar-condicionado está ligado!")
else:
    print("Ar-condicionado desligado!")
