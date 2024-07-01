# Fazer um programa que calcule e imprima o produto por um escalar de uma matriz
# qualquer com dimensões máximas de 20x20.

m = input("Insira o número de linhas da matriz (máximo de 20): ")
n = input("Insira o número de colunas da matriz (máximo de 20): ")
escalar = input("Insira o escalar pela qual a matriz será multiplicada: ")


if m.isdigit() and n.isdigit() and escalar.isdigit():
    m = int(m)
    n = int(n)
    escalar = int(escalar)
    # Verificar se as dimensões da matriz estão dentro do limite máximo
    if m > 20 or n > 20 or m < 0 or n < 0:
        print("As dimensões da matriz excedem o limite máximo permitido.")
    else:
        # Cria a matriz e a matriz após ser multiplicada
        matriz = []
        matriz_mult = []
        print("Insira os elementos da matriz (valores não numéricos serão lidos como 0):")
        for i in range(m):
            linha = []
            linha_mult = []
            for j in range(n):
                elemento = input(f"Insira o elemento da posição ({i + 1}, {j + 1}): ")
                if not elemento.isalpha() and elemento != "":
                    linha.append(float(elemento))
                    linha_mult.append(float(elemento)*escalar)
                else:
                    linha.append(0)
                    linha_mult.append(0)
            matriz.append(linha)
            matriz_mult.append(linha_mult)

        x = f"{escalar} x"
        for i in range(n):
            if matriz.index(matriz[i]) == n//2:
                print(f"{x} {matriz[i]} = {matriz_mult[i]}")
            else:
                print(" "*(len(x)+1) + f"{matriz[i]}   {matriz_mult[i]}")
else:
    print("Valores inválidos")