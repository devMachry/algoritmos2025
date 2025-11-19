
# # linha = 3 
# # colunas = 4
# # matriz = [0] * linha

# #_________________________________________________________________________________________________________
# # Classes
# # Vetor é uma estrutura de dados homogenea unidimensional
# # Uma classe é uma estrutura de dados heterogenea


# class Disciplina:
#     def __init__(self):
#         self.id = 0
#         self.nome = ""
#         self.ch = 0
#         self.professor = ""

# d1 = Disciplina()
# d1.nome = "Algoritmos"

# d2 = Disciplina()
# d2.nome = "Engenharia de Software"

# #_________________________________________________________________________________________________________
# #Listas

# lista = []

# lista.append(5) #insere no fim
# lista.append("Aula")
# lista.append(80.2)

# lista.insert(1, "oi") #insere na posição índice 

# lista.pop(2) #exclui o valor do índice

# lista.remove(80.2)

# print(lista)

# #_________________________________________________________________________________________________________
# #Exercício

# convidados = []

# for i in range(0,6):
#     nomes = input(f"Digite o nome do {i+1}º convidado: ")
#     convidados.append(nomes)

# print("LISTA INICIAL")
# for i in range(0, len(convidados)):
#     print(convidados[i])

# excluir_nome = input("Digite o nome que deseja excluir: ")
# convidados.remove(excluir_nome)


# print("LISTA FINAL")
# for i in range(0, len(convidados)):
#     print(convidados[i])

# #_________________________________________________________________________________________________________

# #Tuplas

# nome = input("Digite o nome do produto: ")
# preco = input("Digite o preço do produto: ")
# qtd = input("Digite a quantidade do produto: ")

# produto = (nome, preco, qtd)

# for i in range(0, len(produto)):
#     print(produto[i])

# print(len(produto))

# #_________________________________________________________________________________________________________

# #Conjuntos

# turma_A = {"Ana", "Beto", "Carlos", "Duda"}
# turma_B = {"Carlos", "Edu", "Fernanda", "Ana"}

# intersecao = turma_A.intersection(turma_B)
# somenteA = turma_A.difference(turma_B)
# uniao = turma_A.union(turma_B)

# print(somenteA)
# print(intersecao)
# print(uniao)

# #_________________________________________________________________________________________________________

# #Dicionários

aluno = {
    "nome" : "Amauri",
    "idade" : 45,
    "curso" : "Apostador"
}

for chave, valor in aluno.items():
    print(f" {chave} : {valor}")


aluno["nota"] = "A"
aluno["idade"] = 50
aluno.pop("curso")

print("DADOS ATUALIZADOS")
for chave, valor in aluno.items():
    print(f" {chave} : {valor}")
