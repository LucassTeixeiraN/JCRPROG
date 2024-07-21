'''11. Uma matriz de permutações é uma matriz quadrada cujos elementos são zeros ou
uns, tal que em cada linha e em cada coluna exista exatamente um elemento igual a 1.
Escreva um programa que, dada uma matriz quadrada, verifique se ela é uma matriz
de permutações.'''

def matriz(n, m):
    # Criação de uma matriz vazia
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            # Solicita ao usuário o valor para a célula (i, j)
            linha.append(int(input(f'matriz[{i+1},{j+1}]: ')))
        matriz.append(linha)
    return matriz

def verificacao(matriz):
    # Obtém o número de linhas e colunas da matriz
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        linha_contagem = 0
        coluna_contagem = 0
        for j in range(colunas):
            # Calcula a soma dos elementos da linha i
            linha_contagem += matriz[i][j]
            # Calcula a soma dos elementos da coluna i
            coluna_contagem += matriz[j][i]
        
        # Verifica se a soma da linha ou coluna não é igual a 1
        if linha_contagem != 1 or coluna_contagem != 1:
            return False
    return True

def main():
    n = int(input("Digite o número de linhas da matriz: "))
    m = int(input("Digite o número de colunas da matriz: "))
    
    print("Digite os elementos da matriz:")
    matriz_original = matriz(n, m)
    
    print("-" * 60)
    print("\nMatriz Original:")
    for linha in matriz_original:
        print(linha)
    
    print()
    if verificacao(matriz_original):
        print("É uma matriz de permutação")
    else:
        print("Não é uma matriz de permutação")
    print("-" * 60)

main()
