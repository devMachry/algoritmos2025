def adicionarNomeNoArquivo(nomeArquivo):
    
        arquivo = open(nomeArquivo, "a", encoding="utf-8")
        
        nome = input("Digite um nome para adicionar ao arquivo: ")
        arquivo.write(nome + '\n')
        
        arquivo.close()
        
        print(f"Nome '{nome}' adicionado com sucesso em '{nomeArquivo}'.")


def lerArquivo(nomeArquivo):
    
    arquivo = open(nomeArquivo, "r", encoding="utf8")

    linhas = arquivo.readlines()
    arquivo.close()
  
    for i in range(len(linhas)):
            linhaAtual = linhas[i]
            print(linhaAtual)

def arquivoFuncionario(dadosFuncionario):
       
       arquivo = open(dadosFuncionario, "a", encoding="utf8")

       nome = input("Digite seu nome: ")
       email = input("Digite seu email: ")
       salario = float(input("Digite seu salário: "))
       dados = arquivo.write(f"{nome}, {email}, {salario},\n")

       arquivo.close()
  

