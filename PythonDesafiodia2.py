# Programa que realize operações básicas de matemática, como adição, subtração, multiplicação e divisão

numero1 = float(input('Escreve um número: '))
numero2 = float(input('Escreve outro número: '))
operacao = input('Qual a operação que quer fazer?(+, -. *, /)')



if operacao == '+':
    soma = numero1 + numero2
    print(f'A soma dos 2 números é {soma}')
elif operacao == '-':
    subtracao = numero1 - numero2
    print(f'A subtração dos 2 números é {subtracao}')
elif operacao == '*':
    multiplicacao = numero1 * numero2
    print(f'A multiplicação dos 2 números é {multiplicacao}')
elif operacao == '/':
    if numero2 == 0:
        print('Não é possivel dividir um número por 0')
    else:
        divisao = numero1 / numero2
        print(f'A divisão dos 2 números é {divisao}')
else:
    print('Essa operação nao existe')










