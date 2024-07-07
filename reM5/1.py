'''Dadas duas listas P1 e P2, ambas com n valores reais que representam as notas de
uma turma na prova 1 e na prova 2, respectivamente, escreva um programa que
calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma
obteve a melhor média.'''

notasP1 = []
notasP2 = []

print("-"*30)
alunos = input("Há quantos alunos na sala?\n")

# Verifica se o número de alunos inserido é válido
if alunos.isnumeric() and int(alunos) > 0:
    alunos = int(alunos)

    print("Insira as notas da primeira prova (Pressione ENTER entre elas):")
    i = 0
    while i < alunos:
        nota = input()

        if not nota.isalpha() and 0 <= float(nota) <= 10:
            nota = float(nota)
            notasP1.append(nota)
            i += 1

    print("Insira as notas da segunda prova (Pressione ENTER entre elas):")
    j = 0
    while j < alunos:
        nota = input()

        if not nota.isalpha() and 0 <= float(nota) <= 10:
            nota = float(nota)
            notasP2.append(nota)
            j += 1


    mediaP1 = sum(notasP1)/len(notasP1)
    mediaP2 = sum(notasP2)/len(notasP2)

    print("-"*25)
    print(f"Notas da P1: {notasP1}")
    print(f"Notas da P2: {notasP2}")
    if mediaP1 > mediaP2:
        print(f"A turma obteve uma média maior na P1, sendo esta {mediaP1:.2f}")
    elif mediaP2 > mediaP1:
        print(f"A turma obteve uma média maior na P2, sendo esta {mediaP2:.2f}")
    else:
        print(f"A média das duas provas foram iguais, sendo esta {mediaP1:.2f}")
    print("-"*25)

else:
    print("Insira um valor numérico válido para o número de alunos")