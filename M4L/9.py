# Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a
# exercícios sobre o mesmo assunto até que ele alcance a nota máxima (100 pontos),
# para só então passar ao assunto seguinte. Entretanto, se após 5 tentativas no mesmo
# nível o aluno obtiver menos de 300 pontos acumulados ele retorna ao nível anterior.
# Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos
# acumulados. Faça um programa que compute o progresso do aluno, através da
# leitura de suas notas até que ele termine o 10º nível. Utilize o comando break (por
# exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota
# máxima)

nivel = 1
pontos_rodada = 0
pontos_acumulados = 0
tentativas = 0

while nivel < 10:

    while tentativas < 5 :
        nota = int(input("Insira seus pontos: "))
        pontos_rodada += nota
        pontos_acumulados += nota
        tentativas += 1

        print("-----------\nNível", nivel, "\nTentativas:", tentativas ,"\nVocê está com", pontos_rodada, "nessa rodada e", pontos_acumulados, "acumulados\n-----------")
        
        if pontos_rodada >= 100:
            nivel += 1
            print("-----------\nVocê subiu de nível\n-----------")
            pontos_rodada = 0
            tentativas = 0
            break

    if tentativas == 5:
        if pontos_acumulados < 300:
            nivel = max(1, nivel - 1)
            tentativas = 0
            pontos_rodada = 0
            pontos_acumulados = 0
            print("--------------------\nNível", nivel, "\nTentativas:", tentativas ,"\nVocê está com", pontos_rodada, "nessa rodada e", pontos_acumulados, "acumulados\n-----------")
        else:
            tentativas = 0
            pontos_rodada = 0
            pontos_acumulados = 0
            print("--------------------\nNível", nivel, "\nTentativas:", tentativas ,"\nVocê está com", pontos_rodada, "nessa rodada e", pontos_acumulados, "acumulados\n-----------")
    else:
        print("--------------------\nNível", nivel, "\nTentativas:", tentativas ,"\nVocê está com", pontos_rodada, "nessa rodada e", pontos_acumulados, "acumulados\n-----------")


print("Parabens!! Você concluiu o desafio!")
