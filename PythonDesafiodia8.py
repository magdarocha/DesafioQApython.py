#Aplicação para gerir uma lista de tarefas, permitindo adicionar e remover itens

def menu():
    print('Lista de tarefas: ')
    print('Opção 1: Adicionar item')
    print('Opção 2: Remover item')
    print('Opção 3: Mostrar a lista')
    print('Opção 4: Sair')
    resposta = input('Escolha um número correspondente às opções acima referidas: ')
    return resposta

lista_geral = []

def adicionar(itens):
    resposta = input(' O que quer adicionar? ')
    itens.append(resposta)

def mostrar(itens):
    if len(itens) == 0:
        print(' A lista está vazia. ')
    else:
        linha = 0
        for l in itens:
            print(linha, ') ', l)
            linha += 1

def remover(itens):
    index = int(input('Qual o index que quer remover? '))
    if len(itens)-1 < index:
        print('Não existe esse item na lista')
    else:
        del itens[index]

while True:
    opcao = menu()
    if opcao == '1':
        adicionar(lista_geral)
    if opcao == '2':
        remover(lista_geral)
    if opcao == '3':
        mostrar(lista_geral)
    if opcao == '4':
        break

