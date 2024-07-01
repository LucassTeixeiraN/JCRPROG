# Elabore um outro programa didático nos mesmos moldes do anterior para treino da
# divisão. Neste programa deve ser perguntado à criança o resultado da divisão e o
# resto

# (19 .Faça um programa didático para estudo de tabuadas de 1 até 10, onde:
# a. A criança escolhe a tabuada a ser estudada.
# b. O programa gera um número aleatório e pergunta à criança qual o valor dele
# multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta
# novamente, se acertar o programa pergunta à criança se ela deseja continuar
# respondendo.
# c. Ao final, o programa deve imprimir o número de perguntas respondidas, o
# número de acertos e o número de erros cometidos pela criança.)


import random

numero_aleatorio1 = int(random.random() * 10)
numero_aleatorio2 = int(random.random() * 10)

numero_respostas = numero_acertos = numero_erros = 0

while True:

    if numero_aleatorio1 != 0 and numero_aleatorio2 != 0: 
        numero_respostas += 1

        divisao_correta = int(numero_aleatorio1 / numero_aleatorio2)
        resto_correto = numero_aleatorio1 % numero_aleatorio2

        resposta_divisao = int(input(str(numero_aleatorio1) + " ÷ " + str(numero_aleatorio2) + "= \nQuociente: "))
        resposta_resto = int(input("Resto: "))

        if resposta_divisao == divisao_correta and resposta_resto == resto_correto:
            numero_acertos += 1
            FIM = int(input("Você Acertou!! Deseja continuar com o exercício?\n1-Sim\n2-Não\n"))
            if FIM == 2:
                break
            else:
                numero_aleatorio1 = int(random.random() * 10)
                numero_aleatorio2 = int(random.random() * 10)
        else: 
            numero_erros += 1
            print("Você errou, tente novamente")
    else:
        numero_aleatorio1 = int(random.random() * 10)
        numero_aleatorio2 = int(random.random() * 10)

print("Você respondeu " + str(numero_respostas) + " perguntas,\nAcertou " + str(numero_acertos) + " e errou " + str(numero_erros))
        