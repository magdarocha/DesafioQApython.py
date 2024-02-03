#programa que funcione como uma agenda de contatos. 
#Deve ser possível adicionar, listar, buscar e excluir contatos.
# Cada contato deve ter nome, número de telefone e e-mail.

def menu():
    print('1) Adicionar contacto')
    print('2) Mostrar contactos')
    print('3) Procurar contactos')
    print('4) Excluir contactos')
    print('5) Sair da agenda')
    opcao = input('Escolha uma das opções: ')
    return opcao

agenda = []

def adicionar(agenda):
    nome = input(' Qual é o nome da pessoa? ')
    numero = input(' Qual é o numero da pessoa? ')
    email = input(' Qual é o email da pessoa? ')

    contacto = dict()
    contacto['nome'] = nome
    contacto['numero'] = numero
    contacto['email'] = email

    agenda.append(contacto)

def mostrar(agenda):
    for i in agenda:
        print(f"O {i['nome']} tem o contacto {i['numero']} e o email {i['email']}. ")

def procurar(agenda):
    nome_procura = input('Escreva o nome do contacto que quer procurar: ')
    encontrei = False
    for i in agenda:
        if i['nome'] == nome_procura:
           print(f"O {i['nome']} tem o contacto {i['numero']} e o email {i['email']}. ")
           encontrei = True
           break

    if encontrei == False:
        print('Este contacto não existe ') 

def excluir(agenda):
    nome_excluir = input('Escreva o nome do contacto que quer excluir: ')
    encontrei = False
    for i in agenda:
        if i['nome'] == nome_excluir:
            agenda.remove(i)
            print('O contacto foi excluido.')
            encontrei = True
            break

    if encontrei == False:
        print('Este contacto não existe ') 

while True:
    opcao = menu()
    if opcao == '1':
        adicionar(agenda)
    if opcao == '2':
        mostrar(agenda)
    if opcao == '3':
        procurar(agenda)
    if opcao == '4':
        excluir(agenda)
    if opcao == '5':
        break