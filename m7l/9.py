'''Escreva um programa que lê duas notas de vários alunos e armazena tais notas em
um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar
quando for lida uma string vazia como nome. Seu programa deve também calcular a
média do aluno e exibir o nome e a média do aluno de maior média.'''

alunos = {}
maior_media = 0
alunos_maiores_medias = []

print("-"*60)
i = 1
while True:
    nome = input(f"Insira o nome do {i}° aluno (Deixe em braco caso não tenha mais alunos): ")
    if nome == "":
        break
    n1 = input(f"Insira a 1° nota do {i}° aluno: ")
    n2 = input(f"Insira a 2° nota do {i}° aluno: ")

    if not n1.isalpha() and 0 <= float(n1) <= 10 and not n2.isalpha() and 0 <= float(n2) <= 10:
        notas = {
            "n1": float(n1), 
            "n2": float(n2), 
        }

        alunos[nome] = notas

        i += 1
    else:
        print("Insira notas com valores reais de 0 a 10")


for chave in alunos.keys():
    soma = 0
    for (nome, nota) in alunos[chave].items():
        soma += nota
    
    media = soma/2
    if media >= maior_media:
        maior_media = media
        alunos_maiores_medias.append(chave)

print("-"*60)
if len(alunos_maiores_medias) == 1:
    print(f"O aluno com a maior média foi {alunos_maiores_medias[0]}, com a média de {maior_media}")
else:
    print("Os alunos com maiores médias foram:")
    for i in alunos_maiores_medias:
        print(i)
    print(f"Com a média de {maior_media}")

