# Escreva um programa que simula o jogo conhecido como “Pedra, Papel e Tesoura”
# de um jogador A contra um jogador B. O programa deve ler a escolha do jogador A e
# a escolha do jogador B. Por fim, o programa deve indicar quem foi o vencedor.

jogador1 = int(input("Jogada do jogador 1:\n1-Pedra\n2-Papel\n3-Tesoura\n"))
jogador2 = int(input("Jogada do jogador 2:\n1-Pedra\n2-Papel\n3-Tesoura\n"))

if(jogador1 == 1): #jogador 1 joga pedra
    if(jogador2 == 2):
        print("O Jogador 2 venceu!")
    elif(jogador2 == 3):
        print("O Jogador 1 venceu!")
    else:
        print("Empate")
elif(jogador1 == 2): #jogador 1 joga papel
    if(jogador2 == 2):
        print("Empate")
    elif(jogador2 == 3):
        print("O Jogador 2 venceu!")
    else:
        print("O Jogador 1 venceu!")
elif jogador1 == 3: #jogador 1 joga tesoura
    if(jogador2 == 2):
        print("O Jogador 1 venceu!")
    elif(jogador2 == 3):
        print("Empate")
    else:
        print("O Jogador 2 venceu!")
else:
    print("selecione uma das três opções para jogar")
