import os
# tamanho = 0
# while(tamanho <= 5):
#     nomeEmail = input("Digite um nome de usuário para o email: ")
#     tamanho = len(nomeEmail)
#     if(tamanho <= 5):
#         print("Informe um email maior que 5 caracteres!")

# print("Digite uma opção de dominio do seu E-mail: ")
# print("1: @ifpr.edu.br")
# print("2: gmail.com")
# print("3: hotmail.com")
# print("4: outro")

# dominio = int(input("Digite o dominio desejado: "))

# if(dominio == 1):
#     email = nomeEmail + "@ifpr.edu.br"

# elif(dominio == 2):
#     email = nomeEmail + "@gmail.com"

# elif(dominio == 3):
#     email = nomeEmail + "@hotmail.com"

# else:
#     provedor = ""
#     while (not("@" in provedor and ".com" in provedor)):
#         provedor = input("Digite seu dominio com @:")

#     email = nomeEmail + provedor

# print(f"Seu email é: {email}")

tamanho = 0
while(tamanho < 10):
    mensagem = input("Digite uma mensagem para o Commit: ")
    tamanho = len(mensagem)

#Executar comandos no git
email = "wellingtonvenite@gmail.com"

#Configurar o email
c = f"git config user.email \"{email}\""
os.system(c)

#Identificar as mudanças no arquivo
c = f"git add *"
os.system(c)

#Registrar o commit com uma mensagem
c = f"git commit -m \"{mensagem}\""
os.system(c)

#Enviar para os servidores do GitHub
c = "git push"
os.system(c)

