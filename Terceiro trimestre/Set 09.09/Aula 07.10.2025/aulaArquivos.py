arq = open("aula.txt", "r")

conteudo = arq.readlines()

soma = 0

for i in range(0, len(conteudo)):
    soma =+ int(conteudo[i].strip())

print(soma)

arq.close()


