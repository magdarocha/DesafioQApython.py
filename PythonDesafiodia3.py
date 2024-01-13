# Verificar se uma palavra ou frase é um palindromo. ex ovo, radar

frase = input('Escreva uma palavra ou frase:' )
frase = frase.lower()
frase = frase.replace(' ' , '')
frase = frase.replace(',', '')
frase = frase.replace('!' , '')
frase = frase.replace('?' , '')

contador = 0
contador1 = -1

while True:
    letra = frase[contador]
    ultima_letra = frase[contador1]
    if letra == ultima_letra:
        contador = contador + 1
        contador1 = contador1 - 1
        if contador == len(frase):
            print('É um palíndromo.')
            break
    else:
        print('Não é um palíndromo.')
        break
    