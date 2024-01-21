#Jogo de adivinhação em que o usuário deve adivinhar um número gerado aleatoriamente pelo programa. O jogo deve ter as seguintes características:
#O programa gera um número aleatório entre 1 e 100.
#O jogador tem um número limitado de tentativas (7) para adivinhar o número correto.
#Após cada tentativa, o programa fornece dicas sobre se o número correto é maior ou menor do que a tentativa atual do jogador.
#O jogo continua até que o jogador adivinhe corretamente o número ou esgote todas as tentativas.

import random


def aleatorio():
    aleatorio = random.randint(1,100)
    print('O computador gerou um numero')
    return aleatorio

def menu_inicial():
    print('1)Jogar')
    print('2)Ver pontuação')
    print('3)Zerar pontuação')
    print('4)Sair')
    resposta = int(input('Escolha uma das opções: '))
    return resposta

pontuacao = 0

while True:
    r = menu_inicial()
    aleatorio1 = aleatorio()
    if r == 1:
        ganhou = False
        for i in range (1,8):
            escolha = int(input('Escolha um número, para tentar adivinhar: '))
            if escolha == aleatorio1:
                print (f'Acertou no número. Tentou {i} vezes.')
                pontuacao += 1
                ganhou = True
                break
            elif escolha < aleatorio1:
                print('O número correto é maior')
            elif escolha > aleatorio1:
                print('O número correto é menor')
        if ganhou == False:
            print('Não ganhou')        
    if r == 2:
        print(f'A sua pontuação é {pontuacao}.')
    if r == 3:
        pontuacao = 0
    if r == 4:
        break


    


