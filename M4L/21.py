# Faça um programa didático para estudo das raízes quadradas dos números, da
# seguinte forma: o programa gera um número aleatório, eleva ao quadrado e pergunta
# qual a raiz quadrada desse valor para o estudante. O programa deve apresentar as
# mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma
# semelhante aos anteriores. 
import random

numero_aleatorio = int(random.random() * 10)
numero_respostas = numero_acertos = numero_erros = 0

while True:
    numero_ao_quadrado = numero_aleatorio ** 2
    numero_respostas += 1

    resposta_usuario = int(input("Qual a raiz quadrada de " + str(numero_ao_quadrado) + " "))

    if resposta_usuario == numero_aleatorio:
        numero_acertos += 1
        FIM = int(input("Você Acertou!! Deseja continuar com o exercício?\n1-Sim\n2-Não\n"))
        if FIM == 2:
            break
        else:
            numero_aleatorio = int(random.random() * 10)
    else: 
        numero_erros += 1
        print("Você errou, mas continue tentando")

print("Você respondeu " + str(numero_respostas) + " perguntas,\nAcertou " + str(numero_acertos) + " e errou " + str(numero_erros))