'''11. Uma matriz de permutações é uma matriz quadrada cujos elementos são zeros ou
uns, tal que em cada linha e em cada coluna exista exatamente um elemento igual a 1.
Escreva um programa que, dada uma matriz quadrada, verifique se ela é uma matriz
de permutações.'''
def Matriz(n,m):
    matriz = []
    for i in range(n):
        linha = []
        
        
        for j in range(m):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz
def Verificacao(Matriz):
    
    linhas = len(Matriz)
    colunas = len(Matriz[0])
    for i in range(linhas):
        linha_contagem = 0
        coluna_contagem =0
        for j in range(colunas):
            linha_contagem += Matriz[i][j]
            coluna_contagem += Matriz[j][i]
        
        if linha_contagem != 1 or coluna_contagem != 1:
            return False 
    return True
    
def main():
    n = int(input("Digite o número de linhas da matriz: "))
    m = int(input("Digite o número de colunas da matriz: "))
    
    print("Digite os elementos da matriz:")
    matriz_original = Matriz(n, m)
    
    print("\nMatriz Original:")
    for linha in matriz_original:
        print(linha)
    
    if Verificacao(matriz_original) == True:
        print("E uma Matriz de permutacao")
    else:
        print("Nao e de permutacao")
    
   

if __name__ == "__main__":
    main()
