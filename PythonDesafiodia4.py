# Programa que conte o número de palavras num texto fornecido pelo utilizador.
#O programa deve ser capaz de separar palavras num texto e determinar quantas palavras estão presentes

texto = input(' Escreva uma frase: ')

texto = texto.strip()

lista = texto.split(' ')

contador = 0

for p in lista:
    if p != '':
        contador = contador + 1





print (f' O texto tem {contador} palavras. ')

