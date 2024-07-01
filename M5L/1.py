# Dadas duas listas P1 e P2, ambas com n valores reais que representam as notas de
# uma turma na prova 1 e na prova 2, respectivamente, escreva um programa que
# calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma
# obteve a melhor média.

n = input("Informe quantos alunos tem na turma: ")
p1 = []
p2 = []

lista = [0,1,2,3,4,5,6,7,8,9,"."]

# Verifica se o número de alunos é um número inteiro maior que zero
if n.isnumeric() and int(n) > 0:
    n = int(n)

    # Loop que funciona até o usuário inserir as notas das 2 provas de todos os alunos
    i = 0
    while i < n * 2:
        if i < n:
            nota = input("Insira as notas da primeira prova (Insira valores reais): ")
        else:
            nota = input("Insira as notas da segunda prova (Insira valores reais): ")

        # Verifica se as notas são número reais entre 0 e 10, inclusive


        if nota.isalpha():
            print("Valor inválido")

        else:
            nota = float(nota)
            if nota <= 10 and nota >= 0:

                # A primeira metade do n é referente à primeira prova, e a segunda à segunda prova
                if i < n:
                    p1.append(nota)
                else:
                    p2.append(nota)
                    
                i += 1
            else:
                print("Insira valores de 0 a 10")

    # Calcula a média das duas provas
    media_p1 = sum(p1)/n
    media_p2 = sum(p2)/n

    print("-"*12)
    print("Prova 1: ")
    print("notas:", p1)
    print("Média:", media_p1)
    print("-"*12)
    print("Prova 2: ")
    print("notas:", p2)
    print("Média:", media_p2)
    print("-"*12)
    if media_p1 > media_p2:
        print("A média da primeira prova foi maior que da segunda")
    else:
        print("A média da segunda prova foi maior que da primeira")

else:
    print("Insira um valor inteiro maior que zero")