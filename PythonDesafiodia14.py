#Gerar senhas aleatorias com criterios especificados pelo utilizador, como comprimento e inclusão de numeros, letras maiusculas, minusculas e caracteres especiais

import random

carateres = int(input('Vamos criar uma password. Quantos caracteres quer? '))
usar_numeros = input('Quer numeros na password? [S/N]: ').upper()
usar_maiusculas = input('Quer usar maiusculas na password? [S/N]: ').upper()
usar_carateresesp = input('Quer usar carateres especiais na password? [S/N]: ').upper()

numeros = [0,1,2,3,4,5,6,7,8,9]
letras = ['A','B']
letras_min = ['a','b']
carateres_especiais = ['%','&', '@']

lista_pos = []
lista_pos.extend(letras_min)

if usar_numeros == 'S':
    lista_pos.extend(numeros)
if usar_maiusculas == 'S':
    lista_pos.extend(letras)
if usar_carateresesp == 'S':
    lista_pos.extend(carateres_especiais)


senha = ''

for i in range(0,carateres):
    senha = senha + str(lista_pos[random.randint(0,len(lista_pos))])

print(senha)