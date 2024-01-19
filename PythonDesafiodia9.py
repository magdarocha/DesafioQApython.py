#Jogo que gera aleatoriamente um número e o jogador deve determinar se esse número é primo ou não. O jogador ganha pontos por cada resposta correta
import random

def aleatorio():
    print('Numero gerado:')
    aleatorio = random.randint(0,200)
    print(aleatorio)
    return aleatorio

def jogo():
    print('O jogador pretende:')
    print('1) Jogar')
    print('2) Ver pontuação')
    print('3) Zerar pontuação')
    print('4) Sair')
    resposta = int(input(' Escolha uma das opções: '))
    return resposta



def primo(aleatorio):
    contagem = 0
    seprimo = False
    for i in range( 1 , aleatorio+1):
        resto = aleatorio%i
        if resto == 0:
            contagem = contagem +  1
    if contagem <= 2:
        print(' É um número primo ')
        seprimo = True
    else:
        print (' Não é um número primo ')
        seprimo = False

    return seprimo


ponto = 0

while True:
    r = jogo()
    if r == 1:
        a = aleatorio()
        escolha = input('Diga se o número gerado anteriormente é primo ou não. Escolha S para sim e N para não').upper()
        sePrimo = primo(a)
        
        if escolha == 'S' and sePrimo == True:
            print('Ganhou 1 ponto')
            ponto += 1
        elif escolha == 'N' and sePrimo == True:
            print('Não ganhou nenhum ponto')
        elif escolha == 'S' and sePrimo == False:
            print('Não ganhou nenhum ponto')
        elif escolha == 'N' and sePrimo == False:
            print('Ganhou 1 ponto')
            ponto += 1
        else:
            print('A opção não existe')
    if r == 2:
        print(f'O jogador tem {ponto} pontos.')

    if r == 3:
        ponto = 0
    if r == 4:
        break



