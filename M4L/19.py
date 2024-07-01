# Faça um programa didático para estudo de tabuadas de 1 até 10, onde:
# a. A criança escolhe a tabuada a ser estudada.
# b. O programa gera um número aleatório e pergunta à criança qual o valor dele
# multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta
# novamente, se acertar o programa pergunta à criança se ela deseja continuar
# respondendo.
# c. Ao final, o programa deve imprimir o número de perguntas respondidas, o
# número de acertos e o número de erros cometidos pela criança
import random

numero_aleatorio = int(random.random() * 10)

tabuada = int(input("Qual tabuada do 1 ao 10 você quer estudar? "))
numero_respostas = numero_acertos = numero_erros = 0

while True:
    numero_respostas += 1

    resposta_correta = tabuada * numero_aleatorio
    resposta_usuario = int(input(str(numero_aleatorio) + " x " + str(tabuada) + "= "))

    if resposta_correta == resposta_usuario:
        numero_acertos += 1
        FIM = int(input("Você Acertou!! Deseja continuar com o exercício?\n1-Sim\n2-Não\n"))
        if FIM == 2:
            break
        else:
            numero_aleatorio = int(random.random() * 10)
    else: 
        numero_erros += 1
        print("Você errou, tente novamente")

print("Você respondeu " + str(numero_respostas) + " perguntas,\nAcertou " + str(numero_acertos) + " e errou " + str(numero_erros))
        
