'''Escreva um programa que recebe como entrada um número inteiro n. Em seguida,
seu programa deve receber as informações de n pessoas (nome, CPF e idade). Para
cada pessoa seu programa deve armazenar as informações utilizando uma estrutura
de dicionário. Infelizmente, algumas entradas do cadastro podem estar repetidas e
você deve removê-las (utilize a chave CPF para isso). No fim, seu programa deve
imprimir a lista de pessoas, sem repetições. Ao remover as repetições mantenha
sempre o primeiro registro lido da pessoa.'''

n = input("Insira quantas pessoas serão lidas: ")
pessoas = {}

if n.isnumeric() and int(n) > 0:
    n = int(n)
    i = 1
    while i <= n:
        nome = input(f"Insira o nome do {i}° indivíduo: ")
        cpf = input(f"Insira o CPF do {i}° indivíduo (insira apenas os números): ")
        idade = input(f"Insira a idade {i}° do indivíduo: ")

        if cpf.isnumeric() and len(cpf) == 11 and idade.isnumeric() and int(idade) >= 0:
            i += 1
            if cpf not in pessoas:
                pessoas[cpf] = {
                    "nome": nome,
                    "idade": idade
                }
        else:
            print("Dados inválidos")

    print("-"*30)
    for (chave, valor) in pessoas.items():
        print("Nome:",valor["nome"])
        print("CPF:",chave)
        print("Idade:",valor["idade"])
        print("-"*30)