#desenvolver um construtor de consultas SQL, um programa em Python que permite aos usuários 
#criar consultas SQL SELECT personalizadas, comandos SQL UPDATE e comandos SQL INSERT. 
#O construtor oferece uma interface interativa para coletar informações 
#e gerar consultas ou comandos SQL com base nas escolhas dos usuários.

def menu():
    print("1) Escolha o SQL SELECT")
    print("2) Escolha o SQL UPDATE")
    print("3) Escolha o SQL INSERT")
    print("4) Sair")
    opcao = input("Qual a opção? ")
    return opcao

def select():
    colunas = input("Quais as colunas? (separe por virgulas) ")
    tabela = input("Qual é a tabela? ")
    condicao = input("Defina uma condição: ")

    query = f"SELECT {colunas} FROM {tabela} WHERE {condicao}"
    print(f"A query é: {query}")

def update():
    tabela = input("Qual é a tabela? ")
    coluna = input("Qual a coluna? ")
    valor = input("Qual o valor para a coluna? ")
    condicao = input("Defina uma condição: ")

    query = f"UPDATE {tabela} SET {coluna} = {valor} WHERE {condicao}"
    print(f"A query é: {query}")

def insert():
    tabela = input("Qual é a tabela? ")
    colunas = input("Quais as colunas? (separe por virgulas) ")
    valores = input("Quais os valores a inserir? (separe por virgulas na ordem das colunas) ")

    query = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
    print(f"A query é: {query}")

while True:
    opcao = menu()

    if opcao == "1":
        select()
    if opcao == "2":
        update()
    if opcao == "3":
        insert()
    if opcao == "4":
        break