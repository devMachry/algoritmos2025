arquivo = open("D:\\Disc. Algoritimos e Estrutura de Dados\\algoritmos2025\\dados.txt" , "r", encoding="utf8")

conteudo = arquivo.readlines()

print(conteudo)

arquivo.close()

qtd = len(conteudo)

for i in range(0, len(conteudo)):
    print(conteudo[i], end="")