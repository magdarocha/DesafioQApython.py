# Programa que peça ao utilizador para inserir um número. 
#O programa deve verificar se o número é par ou impar e exibir uma mensagem a informar

numero = int(input('Insira um número: '))

if numero%2==0:
    print ('O número é par ')
else:
    print(' O número é impar ')