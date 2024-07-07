'''Faça um programa que leia nomes de alunos e suas respectivas notas até que o
nome ’oooo’ seja informado, após o fim da leitura, exiba o nome do aluno que possui
a maior nota. Obs.: Use dicionário para resolver essa questão
'''

PARADA = "oooo"
alunos = []
maior_nota = 0
aluno_maior_nota = ''

while True:
    nome = input("Insira o nome do aluno (Insira 'oooo' para parar): ")
    if nome == PARADA:
        break
    nota = input("Insira a nota do aluno: ")

    if not nota.isalpha() and 0 <= float(nota) <= 10:
        nota = float(nota)

        dic = {
            'nome': nome,
            'nota': nota,
        }
        
        alunos.append(dic)
    else:
        print("Nota inválida")


for i in alunos:
    if i['nota'] > maior_nota:
        maior_nota = i['nota']
        aluno_maior_nota = i['nome']

print("-"*30)
print(f"O aluno com a maior nota é {aluno_maior_nota}")
print("-"*30)
