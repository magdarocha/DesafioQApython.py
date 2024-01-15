# Criar um script que gera e exibe uma lista com 6 números aleatórios entre 1 e 60 (não podem existir números repetidos)

import random

numeros_aleatorios = []

while True:
    numero = random.randint(1,61)

    if numero in numeros_aleatorios:
        pass
    else:
        numeros_aleatorios.append(numero)

    if len(numeros_aleatorios)==6:
        break


print(f'Os seus números aleatórios são estes: {numeros_aleatorios}')