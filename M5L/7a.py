# Fazer um programa que calcule e imprima a soma de duas matrizes (a ordem das
# duas matrizes deve ser lida da entrada padrão).

m = input("Insira quantas linhas a matriz terá: ")
n = input("Insira quantas colunas a matriz terá: ")
m1 = []
m2 = []
m3 = []

# Verifica se m e n são números
if m.isdigit() and n.isdigit():
    m = int(m)
    n = int(n)

    matriz_id = "primeira"
    k = l = 1
    print("Insira os elementos da matriz (qualquer valor não numérico será lido como 0)")
    # Cria duas matrizes com valores fornecidos pelo usuário
    for i in range(m*2):
        linha = []

        for j in range(n):
            elemento = input(f"Insira o elemento da posição ({k}, {l}) da {matriz_id} matriz: ")
            if not elemento.isalpha() and elemento != "":
                linha.append(float(elemento))
                l += 1
            else: 
                linha.append(0)
                l += 1

        # Condicional para decidir qual em qual matriz a linha será adicionada 
        if i < m:
            m1.append(linha)
        else:
            m2.append(linha)
        
        # Redefine l para 1 a cada linha
        l = 1
        k += 1

        # Redefine k para 1 e muda a String da variável matriz_id quando o loop chega na metade
        if i == m-1:
            k = 1
            matriz_id = "segunda"

    # Cria uma terceira matriz que é resultado da soma das outras duas
    for i in range(m):
        linha = []
        for j in range(n):
            elemento = m1[i][j] + m2[i][j]
            linha.append(elemento)
        m3.append(linha)

    print('-'*50)
    
    # Imprime as três matrizes
    for i in range(m):
        linha = []
        if i == m//2:
            elemento = f"{m1[i]} + {m2[i]} = {m3[i]}"
            print(elemento)
        else:
            elemento = f"{m1[i]}   {m2[i]}   {m3[i]}"
            print(elemento)


else:
    print("Os valores inseridos não são válidos")    