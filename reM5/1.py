# Dadas duas listas P1 e P2, ambas com n valores reais que representam as notas de
# uma turma na prova 1 e na prova 2, respectivamente, escreva um programa que
# calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma
# obteve a melhor média.

notasP1 = []
notasP2 = []

print("-"*25)
alunos = input("Há quantos alunos na sala?\n")

# Verifica se o número de alunos inserido é válido
if not alunos.isalpha() and alunos.find(".") == -1 and int(alunos) > 0 :
    alunos = int(alunos)

    for i in range(alunos*2):
        if i == 0:
            print("Insira as notas da primeira prova")
        elif i == alunos:
            print("Insira as notas da segunda prova")

        nota = input()

        if not nota.isalpha():
            nota = float(nota)
        else:
            nota = 0        

        if i < alunos:
            notasP1.append(nota)
        else:
            notasP2.append(nota)
    
else:
    print("Insira um valor númerico válido para o número de alunos")

mediaP1 = sum(notasP1)/len(notasP1)
mediaP2 = sum(notasP2)/len(notasP2)

print("-"*25)
print(notasP1)
print(notasP2)
print("\n")
if mediaP1 > mediaP2:
    print("A turma obteve uma média maior na P1, sendo esta", mediaP1)
else:
    print("A turma obteve uma média maior na P2, sendo esta", mediaP2)
print("-"*25)


