'''Escreva um programa que recebe como entrada um número inteiro n. Em seguida,
seu programa deve receber as informações de n pessoas (nome, CPF e idade). Para
cada pessoa seu programa deve armazenar as informações utilizando uma estrutura
de dicionário. Infelizmente, algumas entradas do cadastro podem estar repetidas e
você deve removê-las (utilize a chave CPF para isso). No fim, seu programa deve
imprimir a lista de pessoas, sem repetições. Ao remover as repetições mantenha
sempre o primeiro registro lido da pessoa.'''


n = int(input("Insira quantas pessoas serão lidas"))
pessoas = {}

i = 0
while i < n:
    nome = input("Insira o nome do indivíduo: ")
    cpf = input("Insira o CPF do indivíduo: ")
    idade = int(input("Insira a idade do indivíduo: "))


    if cpf not in pessoas:
        pessoas[cpf] = {
            "nome": nome,
            "idade": idade
        }

    i += 1

print("-"*30)
print("Dicionário:\n", pessoas)
print("-"*30)
