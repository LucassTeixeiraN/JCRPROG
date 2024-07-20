'''11. Uma matriz de permutações é uma matriz quadrada cujos elementos são zeros ou
uns, tal que em cada linha e em cada coluna exista exatamente um elemento igual a 1.
Escreva um programa que, dada uma matriz quadrada, verifique se ela é uma matriz
de permutações.'''

def matriz(n,m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(int(input(f'matriz[{i+1},{j+1}]: ')))
        matriz.append(linha)
    return matriz

def verificacao(matriz):
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        linha_contagem = 0
        coluna_contagem = 0
        for j in range(colunas):
            linha_contagem += matriz[i][j]
            coluna_contagem += matriz[j][i]
        
        if linha_contagem != 1 or coluna_contagem != 1:
            return False 
    return True
    
def main():
    n = int(input("Digite o número de linhas da matriz: "))
    m = int(input("Digite o número de colunas da matriz: "))
    
    print("Digite os elementos da matriz:")
    matriz_original = matriz(n, m)
    
    print("-"*60)
    print("\nMatriz Original:")
    for linha in matriz_original:
        print(linha)
    
    print()
    if verificacao(matriz_original) == True:
        print("É uma matriz de permutação")
    else:
        print("Não é uma matriz de permutação")
    print("-"*60)
    
main()
