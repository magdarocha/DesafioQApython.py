#Programa em Python que funcione como uma calculadora de despesas pessoais. 
#O programa deve permitir ao usuário registrar suas despesas diárias, categorizá-las e, em seguida, 
#gerar um resumo das despesas por categoria e o total das despesas de uma data específica.

import csv

def ler_csv(nome_da_lista_despesas, despesas):
    """Vai ler o ficheiro CSV"""

    with open(nome_da_lista_despesas) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')

        #10|carro|transporte,10/02/2023
        #15,carro,transporte,11/02/2023

        for row in csv_reader:
            if row:
                despesa = dict()
                despesa['valor']= float(row[0])
                despesa['descricao']= row[1]
                despesa['categoria']= row[2]
                despesa['data']= row[3]

                despesas.append(despesa)

def escrever_csv(nome_da_lista_despesas,despesas):
    """Escrever no ficheiro csv"""
    with open(nome_da_lista_despesas, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|')

        #10|carro|transporte|10/02/2023

        for row in despesas:
            despesa =[]
            despesa.append(row['valor'])
            despesa.append(row['descricao'])
            despesa.append(row['categoria'])
            despesa.append(row['data'])
            csv_writer.writerow(despesa)


def menu():
    print('1)Adicionar despesa: ')
    print('2)Visualizar despesa: ')
    print('3)Sair do menu: ')
    despesa = input('Escolha uma das opções do menu! ')
    return despesa

despesas=[]

def adicionar(despesas):
    valor =  float(input('Qual o valor da despesa? '))
    descricao = input('Descreva a despesa: ')
    categoria = input('Em que categoria se insere? ')
    data = input('Em que data fez esta despesa? ')
    
    despesa = dict()
    despesa['valor']=valor
    despesa['descricao']=descricao
    despesa['categoria']=categoria
    despesa['data']=data

    despesas.append(despesa)

def visualizar(despesas):
    dia = input('Quer ver a despesa por dia?[S/N]').upper()
    categoria = input('Quer ver a despesa por categoria? [S/N]').upper()

    total= 0

    if dia == 'S':
        dia= input('Qual é o dia da despesa?')
        for i in despesas:
            if i['data'] == dia:
                total += i['valor']
    elif categoria == 'S':
        categoria = input('Qual é a categoria?')
        for i in despesas:
            if i['categoria'] == categoria:
                total +=i['valor']

    print(f'O total das despesas é {total}.')

ler_csv('nome_da_lista_despesas.csv', despesas)

while True:
    opcao = menu()
    if opcao == '1':
        adicionar(despesas)
    if opcao == '2':
        visualizar(despesas)
    if opcao == '3':
        break


escrever_csv('nome_da_lista_despesas.csv', despesas)
