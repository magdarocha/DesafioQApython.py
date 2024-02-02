
#Verificar se uma string fornecida por um utilizador é um email valido

import re

email=input('Digite um email: ')
email = '"'+ email + '"'
objeto_especial = re.search('"[a-zA-Z][a-zA-Z0-9\.\-_%+]*@[a-zA-Z0-9\-]{2,}\.[a-zA-Z]{2,}"', email)

if objeto_especial:
    print('O email é válido')
else:
    print('O email é inválido')
