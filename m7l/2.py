'''Escreva um programa que recebe como entrada um número inteiro n. Em seguida,
seu programa deve receber as informações de n pessoas (nome, CPF e idade). Para
cada pessoa seu programa deve armazenar as informações utilizando uma estrutura
de dicionário. Infelizmente, algumas entradas do cadastro podem estar repetidas e
você deve removê-las (utilize a chave CPF para isso). No fim, seu programa deve
imprimir a lista de pessoas, sem repetições. Ao remover as repetições mantenha
sempre o primeiro registro lido da pessoa.'''

n = int(input("Insira quantas pessoas serão lidas: "))
pessoas = {}

for i in range(n):
    nome = input("Insira o nome do indivíduo: ")
    cpf = input("Insira o CPF do indivíduo: ")
    idade = input("Insira a idade do indivíduo: ")

    if cpf not in pessoas:
        pessoas[cpf] = {
            "nome": nome,
            "idade": idade
        }

print("-"*30)
for (chave, valor) in pessoas.items():
    print("Nome:",valor["nome"])
    print("CPF:",chave)
    print("Idade:",valor["idade"])
    print("-"*30)