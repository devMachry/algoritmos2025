import psycopg2

nome = input("Digite o nome do produto: ")
preco = input("Digite o preço do produto: ")
data = input("Digite a data de validade: ")

#PASSO 1: Conectar no BD
con = psycopg2.connect(
    host = "localhost",
    database = "mauricio",
    password = "postgres",
    user = "postgres",
    port = 5432
)

# PASSO 2: Obter o manipulador dos dados

cursor = con.cursor()

# PASSO 3: Definir comando SQL e dados
sql = "INSERT INTO produtos (nome, valor, data_validade) VALUES (%s, %s, %s)"

valores = (nome, preco, data)

# PASSO 4: Executar o comando SQL
cursor.execute(sql, valores)
con.commit()

if(cursor.rowcount > 0):
    print("Registro inserido com sucesso!")
else:
    print("Ocorreu um erro ao inserir o registro!")