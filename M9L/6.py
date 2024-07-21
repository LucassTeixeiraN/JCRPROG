'''6. Escreva uma função que recebe duas matrizes (A e B). Se as duas matrizes tiverem
dimensões compatíveis, sua função deve retornar o produto das duas (C = A × B).
Caso contrário, sua função deve retornar uma lista vazia.
'''

def matriz(nome):
    while True:
        try:
            linhas = int(input(f"Informe o número de linhas da matriz {nome}: "))
            colunas = int(input(f"Informe o número de colunas da matriz {nome}: "))
            matriz = []

            print(f"Informe os elementos da matriz {nome}:")
            for i in range(linhas):
                linha = []
                for j in range(colunas):
                        while True:
                            try:
                                elemento = int(input(f"Insira o elemento ({i+1},{j+1}) da matriz {nome}: "))
                                linha.append(elemento)
                                break
                            except ValueError:
                                print("Valor inválido")
                matriz.append(linha)
            return matriz
        except ValueError:
            print("Valor inválido")

def multiplicacaoMatriz(A, B):
    # O número de colunas de A precisa ser igual ao número de linhas de B
    if len(A[0]) != len(B):
        return []

    C = []

    # Preenche a matriz C com zeros para que ela fique com o número de linhas de A e número de colunas de B
    for i in range(len(A)):
        linha = [0] * len(B[0])
        C.append(linha)

    # Faz a multiplicação das linhas da primeira matriz com as colunas da segunda
    for i in range(len(A)):
        for j in range(len(B[0])):
            multip = 0
            for k in range(len(A[0])):
                multip += A[i][k] * B[k][j]
            C[i][j] = multip

    return C

def imprimir_matriz(matriz, nome):
    print()
    print(f"Matriz {nome}:")
    for linha in matriz:
        print(linha)

def main():
    A = matriz("A")
    B = matriz("B")

    # Imprime as matrizes antes de multiplicá-las
    print("-"*60)
    imprimir_matriz(A, "A")
    imprimir_matriz(B, "B")

    # Multiplicação das matrizes
    resultado = multiplicacaoMatriz(A, B)
    
    if resultado != []:
        imprimir_matriz(resultado, "C")
    else:
        print()
        print(f"Matriz C:")
        print([])
    print("-"*60)

main()
