'''4. Escreva uma função que dada uma matriz (M), calcule a sua transposta (Mt).'''
def Transposta(Matriz):
    linhas = len(Matriz)
    colunas = len(Matriz[0])
    Matriz_Transposta = []
    
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(Matriz[i][j])
        Matriz_Transposta.append(nova_linha)
        
    return Matriz_Transposta
    

def Matriz(n,m):
    matriz = []
    for i in range(n):
        linha = []
        
        
        for j in range(m):
            linha.append(input())
        matriz.append(linha)
    return matriz
def main():
    n = int(input("Digite o número de linhas da matriz: "))
    m = int(input("Digite o número de colunas da matriz: "))
    
    print("Digite os elementos da matriz:")
    matriz_original = Matriz(n, m)
    
    print("\nMatriz Original:")
    for linha in matriz_original:
        print(linha)
    
    print("\nMatriz Transposta:")
    matriz_transposta = Transposta(matriz_original)
    for linha in matriz_transposta:
        print(linha)

if __name__ == "__main__":
    main()
