# Desenvolver um script que ordene uma lista de números fornecida pelo usuário

lista = input(' Escreva um conjunto de 5 números inteiros, separados por vírgulas: ')

numeros = lista.split(',')

for i in range(0,len(numeros)):
    numeros[i] = int(numeros[i])

numeros.sort()
print(f'A sua lista ordenada é {numeros}')