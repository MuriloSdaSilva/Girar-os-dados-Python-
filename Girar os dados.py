from random import randint
while True:
    perguntaDados = input("Voce quer jogar o dado? [S/N] ")
    resposta = "S"
    if perguntaDados.upper() == "S":
        while resposta.upper() != "N":
            perguntaDados == "N"
            dados = randint(1, 6)
            print(dados)
            resposta = input('Voce quer jogar novamente? [S/N] ')
        print('Jogador não quer mais girar o dado!')
        break
    elif perguntaDados == "N":
        print("Programa encerrado, jogador não quis girar o dado!")
        break

    elif perguntaDados != "S" or perguntaDados != "N":
        print("Comando invalido, digite novamente!")
        continue





