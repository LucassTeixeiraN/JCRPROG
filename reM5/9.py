# Fazer um programa que calcule e imprima o produto por um escalar de uma matriz
# qualquer com dimensões máximas de 20x20.

matriz = []
matriz_mult = []

m = input("Insira o número de linhas da matriz (máximo 20): ")
n = input("Insira o número de colunas da matriz (máximo 20): ")
escalar = input("Insira o número que multiplicará a matriz: ")

if m.isdigit() and n.isdigit() and not escalar.isalpha() and escalar != "" and 0 < int(m) <= 20 and 0 < int(n) <= 20:
    m = int(m)
    n = int(n)
    escalar = float(escalar)

    print("Insira os números da matriz (pressione Enter entre cada número). Obs: Valores não numéricos serão considerados como 0: ")
    for i in range(m):
        linha = []
        linha_mult = []
        for j in range(n):
            elemento = input()

            if not elemento.isalpha() and elemento != "":
                elemento = float(elemento)
                linha.append(elemento)
                linha_mult.append(elemento*escalar)
            else:
                linha.append(0)
                linha_mult.append(0)
        matriz.append(linha)
        matriz_mult.append(linha_mult)


    print("-"*75)
    for i in range(m):
        if i == m//2:
            print(f"{escalar} x {matriz[i]} = {matriz_mult[i]}")
        else:
            print(f"{len(str(escalar))*" "}   {matriz[i]}   {matriz_mult[i]}")
    print("-"*75)


else:
    print("-"*75)
    print("Tente inserir valores numéricos inteiros positivos e menores ou igual a 20 na ordem das matrizes e um número real para multiplicar a matriz")
    print("-"*75)
