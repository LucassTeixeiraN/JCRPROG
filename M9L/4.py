'''4. Escreva uma função que dada uma matriz (M), calcule a sua transposta (Mt).'''

def matriz(n, m):
    # Cria uma matriz vazia
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            # Solicita entrada do usuário e adiciona ao elemento da linha atual
            linha.append(input())
        matriz.append(linha)
    return matriz

def Transposta(matriz):
    # Obtém o número de linhas e colunas
    linhas = len(matriz)
    colunas = len(matriz[0])
    Mt = []
    
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            # Troca as linhas pelas colunas para criar a matriz transposta
            nova_linha.append(matriz[i][j])
        Mt.append(nova_linha)
        
    return Mt

def main():
    n = int(input("Digite o número de linhas da matriz: "))
    m = int(input("Digite o número de colunas da matriz: "))
    
    print("Digite os elementos da matriz:")
    M = matriz(n, m)
    
    print("-" * 60)
    print("\nMatriz Original:")
    for linha in M:
        print(linha)
    
    print("\nMatriz Transposta:")
    Mt = Transposta(M)
    for linha in Mt:
        print(linha)
    print("-" * 60)

main()
