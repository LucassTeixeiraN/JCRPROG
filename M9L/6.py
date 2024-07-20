'''6. Escreva uma função que recebe duas matrizes (A e B). Se as duas matrizes tiverem
dimensões compatíveis, sua função deve retornar o produto das duas (C = A × B).
Caso contrário, sua função deve retornar uma lista vazia.
'''
def Matriz(n,m):
    matriz = []
    for i in range(n):
        linha = []
        
        
        for j in range(m):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz

def produto(Matriz1,Matriz2):
    mlinha1 = len(Matriz1)
    mlinha2 = len(Matriz2)
    mcoluna = len(Matriz1[0])
    if mlinha1 == mlinha2:
        resultado = []
        for i in range(mlinha1):
            linha_resultado = []
            for j in range(mcoluna):
                elemento_resultado = Matriz1[i][j] * Matriz2[i][j]
                linha_resultado.append(elemento_resultado)
            resultado.append(linha_resultado)
        return resultado
    else:
        return False
    
def main():
    n = int(input("Digite o número de linhas da matriz 1: "))
    m = int(input("Digite o número de colunas da matriz 1: "))
    
    print("Digite os elementos da matriz 1:")
    matriz1 = Matriz(n, m)
    
    x = int(input("Digite o número de linhas da matriz 2: "))
    y = int(input("Digite o número de colunas da matriz 2: "))
    
    print("Digite os elementos da matriz 2:")
    matriz2 = Matriz(x,y)
    
    
    print("\nMatriz 1:")
    for linha in matriz1:
        print(linha)
    
    print("\nMatriz 2:")

    for linha in matriz2:
        print(linha)
    
    if not produto(matriz1,matriz2) == False:
        print("\n")
        print("Produto das Matrizes:")
        for linha in produto(matriz1,matriz2):
            print(linha)
    else:
        print("Nao sao iguais")

if __name__ == "__main__":
    main()
