#Versão simples do jogo da forca. 
#O utilizador tenta adivinhar uma palavra escolhida aleatoriamente pelo computador

import random

palavras =['televisao' , 'escrivaninha', 'esfigmomanometro', 'banco', 'cadeira']

def palavra_aleatoria(palavrasaleatorias):
    """Escolher uma palavra aleatória da lista"""
    aleatorio= random.randint(0,len(palavras))
    return palavrasaleatorias[aleatorio]

palavra_do_jogo= palavra_aleatoria(palavras)

letras_certas = []

letras_erradas = []

copia_palavra_jogo = palavra_do_jogo

while True:
    print(letras_erradas)
    letra = input('Escolha uma letra: ').lower()
    if letra in palavra_do_jogo:
        if letra in letras_certas:
            print('Essa letra já foi escrita.')
        else:
            letras_certas.append(letra)
            palavra_do_jogo = palavra_do_jogo.replace(letra,'')
            if palavra_do_jogo:
                pass
            else:
                print(f'Acertou na palavra. A palavra é {copia_palavra_jogo}. ')
                break
    else:
        if letra in letras_erradas:
            print('Essa letra já foi dita')
        else:
            print('Essa letra não faz parte da palavra')
            letras_erradas.append(letra)

            if len(letras_erradas) == 5:
                print('Esgotou as tentativas')
                break

