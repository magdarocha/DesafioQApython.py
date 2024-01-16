#Criar um programa para converter unidades de medida: 
#km para milhas, milhas para km, metros para pés, pés para metros, graus celsius para fahrenheit e graus fahrenheit para celsius
#Quilômetros para Milhas (1 quilômetro = 0,621371 milhas), Milhas para Quilômetros (1 milha = 1,60934 quilômetros), 
#Metros para Pés (1 metro = 3,28084 pés), Pés para Metros (1 pé = 0,3048 metros), 
#Graus Celsius para Fahrenheit (Fahrenheit = Celsius * 9/5 + 32) e Graus Fahrenheit para Celsius (Celsius = (Fahrenheit - 32) * 5/9)


while True:
    pergunta = int(input('Selecione um número de acordo com o seguinte( 1-Km para milhas,2- milhas para km, 3- metros para pés, 4- pés para metros, 5- graus celsius para fahrenheit, 6- fahrenheit para celsius 0- para parar)'))
    if pergunta==1:
#Km para milhas
        km = float(input('Escreva o número em KM: '))
        conversao = 0.621371
        calculo_milhas = (km*conversao)

        print(f'É igual a {calculo_milhas} milhas')
    elif pergunta==2:
#milhas para km
        milhas = float(input('Escreva o número em milhas: '))

        calculo_km =(milhas/conversao)

        print(f'É igual a {calculo_km} km')
    elif pergunta==3:
#metros para pés
        metros = float(input('Escreva o número em metros: '))
        conversao_1 = 3.28084

        calculo_feet = (metros * conversao_1)

        print(f'É igual a {calculo_feet} pés')
    elif pergunta==4:
#pes para metros

        pes = float(input('Escreva o número em pes: '))
        conversao_2 = 0.3048

        calculo_meters = (pes * conversao_2)

        print(f'É igual a {calculo_meters} metros')
    elif pergunta==5:
#Celsius para Fhr
        graus_celsius = float(input('Escreva o número em celsius: '))

        calculo_fahrenheit = (graus_celsius * 9/5)+32

        print(f'É igual a {calculo_fahrenheit} graus Fahrenheit')
    elif pergunta==6:
#Fhr para Celsius

        fahrenheit = float(input('Escreva o número em fahrenheit: '))

        calculo_celsius = (fahrenheit - 32) * 5/9

        print(f'É igual a {calculo_celsius} graus celsius')

    elif pergunta==0:
        break


