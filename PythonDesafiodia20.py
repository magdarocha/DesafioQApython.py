#Desenvolva um pequeno quiz de múltipla escolha com perguntas e respostas. 
#O programa deve mostrar uma pergunta com opções de resposta e permitir que o usuário escolha uma. 
#No final, o programa deve mostrar a pontuação do usuário.

questionario= []

pergunta1 = dict()
pergunta1["pergunta"] = "Qual é a capital do Brasil?"
pergunta1["respostas"] = "1-Lisboa\n2-Porto\n3-Brasilia\n4-Londres"
pergunta1["certa"] = "3"
questionario.append(pergunta1)

pergunta2 = dict()
pergunta2["pergunta"] = "Quem escreveu \"Dom Quixote\"?"
pergunta2["respostas"] = "1-Miguel de Cervantes\n2-Eu\n3-Tu\n4-Eça de Queiroz"
pergunta2["certa"] = "1"
questionario.append(pergunta2)

pergunta3 = dict()
pergunta3["pergunta"] = "Qual é o maior planeta do sistema solar?"
pergunta3["respostas"] = "1-Urano\n2-Júpiter\n3-Plutão\n4-Marte"
pergunta3["certa"] = "2"
questionario.append(pergunta3)

respostas_certas = 0
for pergunta in questionario:
    print(pergunta["pergunta"])
    print(pergunta["respostas"])
    resposta = input("Qual a tua resposta: ")
    if resposta == pergunta["certa"]:
        #print("Resposta está certa")
        respostas_certas += 1
    else:
        print("Resposta está errada")

print(f"Acertaste {respostas_certas} de {len(questionario)}")