import psycopg2

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
sql = "SELECT * FROM produtos"


# PASSO 4: Executar o comando SQL
cursor.execute(sql)

resultado = cursor.fetchall()

for linha in resultado:
    print("ID: ", linha[0])
    print("Nome: ", linha[1])
    print("Valor: ", linha[2])
    print("Data de validade: ", linha[3])

