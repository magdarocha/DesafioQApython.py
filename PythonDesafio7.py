#Criar um programa que funcione como um temporizador (contagem progressiva) ou contador regressivo. O utilizador pode escolher entre as duas opções.
import time

temporizador = input('Escolha um contador progressivo ou regressivo. Escreva P para progressivo e R para regressivo. ').upper()
tempo = int(input('Quanto tempo em segundos quer para o temporizador? '))

contagem = 0
contagem_regressiva = tempo

while True:
    time.sleep(1)
    if temporizador == 'P':
        contagem += 1
        print(contagem)
    elif temporizador == 'R':
        contagem_regressiva -= 1
        print(contagem_regressiva)
    if contagem == tempo or contagem_regressiva == 0:
        break

print('Acabou a contagem.')