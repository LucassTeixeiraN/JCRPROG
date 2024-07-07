# Faça um programa para corrigir uma prova de múltipla escolha de 10 questões, cujo
# gabarito é b, c, d, a, a, e, b, d, a, c. Cada questão vale 1,0 ponto e a nota será de 0,0 a
# 10,0. O programa deve ler do teclado o número de matrícula de até 30 alunos em um
# vetor e suas respectivas respostas em uma matriz (que devem obrigatoriamente estar
# entre ‘a’ e ‘e’. A seguir, o programa deve calcular e imprimir:
# a. Para cada aluno, seu número e nota.
# b. A porcentagem de alunos aprovados, sendo a menor nota para aprovação
# igual a 6,0.

GABARITO = ('b', 'c', 'd', 'a', 'a', 'e', 'b', 'd', 'a', 'c')
matriculas = input("Insira o número de alunos (Max: 30): ")
notas = []
aprovados = 0

if matriculas.isdigit() and 0 < int(matriculas) <= 30:
    matriculas = int(matriculas)

    for i in range(matriculas):
        respostas = []
        nota = 0

        print(f"Insira as respostas do aluno {i+1} (Pressione Enter entre as respostas). Obs: Insira respostas de 'a' a 'e':")
        j = 0
        while j < 10:
            alternativa = input()

            if alternativa in ['a', 'b', 'c', 'd', 'e']:
                respostas.append(alternativa)
                j += 1
            else:
                print("Insira uma resposta válida")
        
        for k in range(10):
            if respostas[k] == GABARITO[k]:
                nota += 1
                
        notas.append(nota)


    for i in notas:
        if i >= 6:
            aprovados += 1
    
    print("-"*60)
    print("Notas:")

    for i in range(matriculas):
        print(f"Aluno {i+1}: {notas[i]}")

    print("-"*60)
    print(f"Porcentagem de aprovados: {(aprovados/matriculas)*100}%")
    print("-"*60)

else:
    print("Número de alunos inválido")