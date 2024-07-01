# Faça um programa que leia as dimensões de uma matriz qualquer (no máximo 30x30),
# leia seus elementos e imprima a sua transposta.

matriz = []
transposta = []

m = input("Insira o número de linhas da matriz (máximo 30): ")
n = input("Insira o número de colunas da matriz (máximo 30): ")

if m.isdigit() and n.isdigit() and 0 < int(m) <= 30 and 0 < int(n) <= 30:
    m = int(m)
    n = int(n)

    print("Insira os números da matriz (pressione Enter entre cada número). Obs: Valores não numéricos serão considerados como 0: ")
    for i in range(m):
        linha = []
        for j in range(n):
            elemento = input()

            if not elemento.isalpha() and elemento != "":
                elemento = float(elemento)
                linha.append(elemento)
            else:
                linha.append(0)
        matriz.append(linha)

    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(matriz[j][i])
        transposta.append(linha)

    for i in range(m):
        print(matriz[i])

    print("-"*60)
    
    for i in range(n):
        print(transposta[i])

else:
    print("-"*75)
    print("Tente inserir valores numéricos inteiros positivos e menores ou igual a 30 na ordem das matrizes")
    print("-"*75)

