#Programa que analise a frequência de cada letra num texto fornecido pelo usuário

texto = input('Escreva uma frase à sua escolha: ').lower()

letras =dict()

for i in range(0,len(texto)):
    caracter = texto[i]
    if caracter.isalpha():
        if caracter in letras:
            letras[caracter] += 1
        else:
            letras[caracter] = 1

print(letras)