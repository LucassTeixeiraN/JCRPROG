# Numa universidade, o sistema de avaliação é o seguinte: para passar direto, o aluno
# precisa ter média do período (mp) igual ou superior a 7 pontos. Caso contrário, o
# aluno será submetido a exame final, sendo a sua média final (mf) calculada pela
# seguinte fórmula: mf = 0.6mp + 0.4ne, onde ne é a nota do exame. Essa média final
# deverá então ser igual ou superior a 5 pontos para que o aluno seja aprovado. Por
# outro lado, a média do período é calculada através da média das notas dos créditos,
# cujo número é diferente para cada disciplina. Faça um programa que leia do usuário o
# número de créditos da disciplina, as notas dos créditos, e se necessário calcule a
# nota que o aluno precisa tirar no exame final para ser aprovado. Se antes de terminar
# todos os créditos o aluno já estiver aprovado, avise isso a ele e encerre a leitura de
# notas (utilize aqui um comando break). 

quantidade_creditos = int(input("Insira o número de créditos da matéria "))
creditos_analisado = soma_notas = 0

while creditos_analisado < quantidade_creditos:
    creditos_analisado += 1
    soma_notas += float(input("Insira suas notas de crédito "))

    mp = soma_notas/quantidade_creditos

    if mp >= 7:
        break

if mp < 7:
    ne = (5 - 0.6*mp)/ 0.4
    print("Ficou de exame")
    print("Você precisa tirar ao menos", ne, "no exame final para passar na diciplina")
else:
    print("Você passou, parabens!")