#Permitir ao utilizador inserir informaçoes sobre livros na sua biblioteca pessoal 
#e a seguir mostrar a lista de livros disponiveis
import csv

def ler_csv(nome_da_lista_livros, lista_livros):
    """Vai ler o ficheiro CSV"""

    with open(nome_da_lista_livros) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            lista_livros.append(row)

def escrever_csv(nome_da_lista_livros,lista_livros):
    """Escrever no ficheiro csv"""
    with open(nome_da_lista_livros, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        for row in lista_livros:
            csv_writer.writerow(row)



livros = []

def menu():
    """Menu para o utilizador adicionar livros, ver livros ou sair """

    adicionar = input('Quer adicionar um livro? [S/N]: ').upper()
    ver_livro = input('Quer ver os livros que tem na lista? [S/N]: ').upper()
    sair = input('Quer sair? [S/N]: ').upper()

    return adicionar, ver_livro, sair

def adicionar_livro(lista_de_livros):
    """Menu com os dados dos livros"""

    nome = input(' Diga o nome do livro: ')
    autor = input(' Diga o autor do livro: ')
    ano = input(' Diga o ano do livro: ')
    lista_de_livros.append([nome,autor,ano])

def ver_os_livros(lista_de_livros):
    """Ver os livros que estão na lista"""

    for i in lista_de_livros:
        print(i)



ler_csv('listadelivros.csv', livros)

while True:
    adicionar, ver_livro, sair= menu()

    if adicionar == 'S':
        adicionar_livro(livros)

    if ver_livro == 'S':
        ver_os_livros(livros)

    if sair == 'S':
        break

escrever_csv('listadelivros.csv', livros)