#Programa que converta valores entre diferentes moedas. 
#O programa deve permitir ao usuário inserir o valor, a moeda de origem e a moeda de destino, e então mostrar o valor convertido utilizando uma api pública que traz a taxa para a conversão.
#Usar uma API

import requests

import json

origem = input('Qual a moeda de origem? ').upper()
destino = input('Qual a moeda de destino? ').upper()
valor = float(input('Qual o valor? '))

x = requests.get(f'https://open.er-api.com/v6/latest/{origem}')

data = json.loads(x.text)

conversao = data['rates'][destino]

valor_destino = valor * conversao

print(f'O valor convertido é {valor_destino}. ')
