'''Escreva uma função que recebe duas matrizes (A e B). Se as duas matrizes tiverem
dimensões compatíveis, sua função deve retornar a soma das duas (C = A + B). Caso
contrário, sua função deve retornar uma lista vazia.'''

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

def somaMatriz(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):  # verifica se as dimensões das matrizes são compatíveis
        return []

    C = [[0 for j in range(len(A[0]))] for i in range(len(A))]  # matriz resultante C com zeros

    for i in range(len(A)):  # soma das matrizes
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]

    return C

def imprimir_matriz(matriz, nome):
    print(f"Matriz {nome}:")
    for linha in matriz:
        print(linha)

def main():

    A = matriz("A")
    B = matriz("B")

    # Imprime as matrizes antes de somá-las
    imprimir_matriz(A, "A")
    imprimir_matriz(B, "B")

    # Soma das matrizes
    resultado = somaMatriz(A, B)
    if resultado:
        print("A soma das matrizes é:")
        imprimir_matriz(resultado, "C")
    else:
        print("As matrizes têm dimensões incompatíveis.")

main()
